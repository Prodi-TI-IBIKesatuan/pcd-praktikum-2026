#!/usr/bin/env bash
# Menyiapkan organisasi GitHub untuk praktikum PCD sesuai panduan prodi.
#
# Yang dikerjakan (aman dijalankan berulang):
#   1. Label issue di repo materi (video, modul, soal, tugas, bug-lab, pekan:NN, ...)
#   2. Tim "dosen-pcd" dan "dls" beserta hak aksesnya ke repo materi
#   3. Ruleset branch main: wajib PR, 1 persetujuan code owner, cek "validasi" lulus
#   4. 14 repo template tugas pcd-tugas-pNN-* (dirakit dari tugas/), ditandai Template
#   5. Tag v1 untuk reusable workflow autograder
#
# Prasyarat: gh CLI sudah login sebagai owner organisasi (gh auth login),
#            python3, git. Jalankan dari akar repo ini.
#
# Pemakaian:
#   DRY_RUN=1 bash tools/setup-github.sh     # hanya tampilkan perintah, tidak mengubah apa pun
#   bash tools/setup-github.sh               # jalankan sungguhan
#   ORG=Org-Lain bash tools/setup-github.sh  # organisasi berbeda
#   PERBARUI_TEMPLATE=1 bash tools/setup-github.sh   # dorong ulang isi template yang sudah ada
set -euo pipefail

ORG="${ORG:-Prodi-TI-IBIKesatuan}"
REPO="${REPO:-pcd-praktikum-2026}"
DRY_RUN="${DRY_RUN:-0}"
PERBARUI_TEMPLATE="${PERBARUI_TEMPLATE:-0}"
AKAR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KERJA="$(mktemp -d)"
trap 'rm -rf "$KERJA"' EXIT

info() { printf '\n== %s\n' "$*"; }
jalankan() {
  if [ "$DRY_RUN" = "1" ]; then
    printf '[dry-run]'; printf ' %q' "$@"; printf '\n'
  else
    "$@"
  fi
}
ada() { [ "$DRY_RUN" != "1" ] && "$@" >/dev/null 2>&1; }

if [ "$DRY_RUN" != "1" ]; then
  command -v gh >/dev/null || { echo "gh CLI belum terpasang: https://cli.github.com" >&2; exit 1; }
  gh auth status >/dev/null || { echo "Jalankan 'gh auth login' dulu." >&2; exit 1; }
fi

# ---------------------------------------------------------------- 1. label
info "1/5 Label issue di $ORG/$REPO"
label() { jalankan gh label create "$1" --repo "$ORG/$REPO" --color "$2" --description "$3" --force; }
label video "1f6feb" "Produksi video materi"
label modul "0e8a16" "Modul tertulis"
label soal "fbca04" "Bank soal kuis Moodle"
label tugas "5319e7" "Template tugas dan tes"
label bug-lab "d73a4a" "Kendala teknis lab (Codespaces, Colab, autograder)"
label "prioritas:tinggi" "b60205" "Harus selesai sebelum rilis Jumat"
label dls "c5def5" "Pekerjaan Digital Learning Squad"
for n in $(seq -w 1 14); do label "pekan:$n" "ededed" "Materi pekan $n"; done

# ---------------------------------------------------------------- 2. tim
info "2/5 Tim dan hak akses"
tim() {
  local slug="$1" nama="$2" izin="$3"
  if ada gh api "orgs/$ORG/teams/$slug"; then
    echo "tim $slug sudah ada"
  else
    jalankan gh api -X POST "orgs/$ORG/teams" -f name="$nama" -f privacy=closed
  fi
  jalankan gh api -X PUT "orgs/$ORG/teams/$slug/repos/$ORG/$REPO" -f permission="$izin"
}
tim dosen-pcd dosen-pcd maintain
tim dls dls push
echo "Tambahkan anggota: gh api -X PUT orgs/$ORG/teams/<tim>/memberships/<username>"

# ---------------------------------------------------------------- 3. ruleset
info "3/5 Ruleset branch main"
RULESET="$KERJA/ruleset.json"
cat >"$RULESET" <<'JSON'
{
  "name": "lindungi-main",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 1,
        "require_code_owner_review": true,
        "dismiss_stale_reviews_on_push": true,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      } },
    { "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [ { "context": "validasi" } ]
      } }
  ]
}
JSON
if [ "$DRY_RUN" != "1" ] && gh api "repos/$ORG/$REPO/rulesets" --jq '.[].name' | grep -qx lindungi-main; then
  echo "ruleset lindungi-main sudah ada"
else
  jalankan gh api -X POST "repos/$ORG/$REPO/rulesets" --input "$RULESET"
fi

# ---------------------------------------------------------------- 4. repo template
info "4/5 Repo template tugas"
python3 "$AKAR/tools/rakit_template.py" --semua "$KERJA/template" >/dev/null
for dir in "$KERJA"/template/pcd-tugas-*; do
  nama="$(basename "$dir")"
  if ada gh repo view "$ORG/$nama"; then
    if [ "$PERBARUI_TEMPLATE" = "1" ]; then
      jalankan git clone -q "https://github.com/$ORG/$nama.git" "$KERJA/klon-$nama"
      if [ "$DRY_RUN" != "1" ]; then
        rsync -a --delete --exclude .git "$dir/" "$KERJA/klon-$nama/"
        git -C "$KERJA/klon-$nama" add -A
        if git -C "$KERJA/klon-$nama" diff --cached --quiet; then
          echo "$nama sudah mutakhir"
        else
          git -C "$KERJA/klon-$nama" commit -qm "tugas: perbarui template dari $REPO"
          git -C "$KERJA/klon-$nama" push -q
          echo "$nama diperbarui"
        fi
      fi
    else
      echo "$nama sudah ada (PERBARUI_TEMPLATE=1 untuk mendorong ulang isinya)"
    fi
  else
    if [ "$DRY_RUN" != "1" ]; then
      git -C "$dir" init -q -b main
      git -C "$dir" add -A
      git -C "$dir" commit -qm "tugas: template awal dari $REPO"
    fi
    jalankan gh repo create "$ORG/$nama" --public --source "$dir" --push \
      --description "Template tugas praktikum PCD ($nama). Jangan dikerjakan di sini: terima lewat tautan Classroom 50."
  fi
  jalankan gh api -X PATCH "repos/$ORG/$nama" -F is_template=true --silent
done

# ---------------------------------------------------------------- 5. tag v1
info "5/5 Tag v1 untuk reusable workflow"
if ada gh api "repos/$ORG/$REPO/git/ref/tags/v1"; then
  echo "tag v1 sudah ada. Untuk memindahkannya ke main terbaru:"
  echo "  git tag -f v1 origin/main && git push -f origin v1"
else
  jalankan git -C "$AKAR" tag v1 origin/main
  jalankan git -C "$AKAR" push origin v1
fi

info "Selesai. Langkah manual yang tersisa:"
cat <<EOF
  - Settings > Secrets and variables > Actions di $ORG/$REPO:
      KUNCI_TOKEN   (secret) fine-grained token baca-saja ke repo privat $ORG/pcd-kunci
      MOODLE_TOKEN  (secret, opsional) token web service Moodle
      MOODLE_URL    (variable, opsional) mis. https://elearning.ibik.ac.id
      MODUL_P01..P14 (variable, opsional) daftar cmid aktivitas Moodle per pekan
  - Organisasi: wajibkan 2FA (Settings > Authentication security).
  - Classroom 50: buat classroom & 14 assignment sesuai docs/classroom50-tes.md.
EOF
