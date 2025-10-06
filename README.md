# Render-Ready Streamlit (Python 3.11)

This repo is pinned to versions that ship **manylinux wheels** for Python **3.11**, avoiding native C/C++ builds on Render.

## Deploy
1. Push these files to a new GitHub repo (root contains `render.yaml`, `runtime.txt`, `requirements.txt`, `app.py`).
2. Create a **Web Service** on Render from that repo.
3. In the first deploy: **Manual Deploy → Clear build cache** then Deploy.
4. Add secrets (Environment tab): BITGET_API_KEY/SECRET/PASSPHRASE, TELEGRAM_BOT_TOKEN/CHAT_ID.

If logs show Python 3.13, you are not at the correct repo root. Ensure `runtime.txt` is at the service root.
