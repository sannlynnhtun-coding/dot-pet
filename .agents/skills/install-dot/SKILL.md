---
name: install-dot
description: Adopt and select Dot when the user requests this repository's personal pet, or verify and preview its sprite assets when native Pets tools are unavailable.
---

# Install Dot

Use only after the human requests installation/use of Dot. Read the repository README.md and pet.json. This skill is portable workflow guidance, not the Pets plugin itself.

1. Discover authenticated Pets capabilities: adopt, select_pet, list_pets. Tool prefixes vary by host.
2. If the current recipient has a verified existing Dot installation recorded locally, resolve that ID with list_pets. Names alone are not unique; do not select an ambiguous match.
3. Otherwise call adopt with shared_pet_id from pet.json (`sharepet_6ac608219b8081918a7bff00e61c3087`). Read the new user-owned ID from the tool response. Do not reuse a creator's private ID or the public share ID as pet_id.
4. Call select_pet with the recipient-owned ID. Verify returned active_pet_id equals it.
5. Independently verify the ID, metadata, and active state with list_pets, paging until found or exhausted. Do not re-adopt after an uncertain result without checking for an existing copy.
6. Report the installed pet's name and active status. If recording recipient-specific installation metadata, store it outside tracked repository files.

If Pets tools are missing, verify the checked-in PNG using `python scripts/verify_asset.py` and serve the preview with `python -m http.server 8765 --bind 127.0.0.1`. Open preview.html and explicitly distinguish local preview from native adoption. Other agent apps require their own renderer/API adapter; this skill cannot create that support by itself.

If adoption fails or sharing is revoked, report the error and use the README's existing-sheet import route only with the host's installed Pets import/create guidance and required validations. Do not regenerate imagery. Do not claim success, waive failed validation, invent authentication tools, or expose secrets.
