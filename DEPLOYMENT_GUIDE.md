# 🚀 Streamlit Cloud Deployment Guide

## Step 1: Prepare Your Repository

Your code is already on GitHub at: `https://github.com/adeelciit786-hue/bank.git`

Make sure your `.gitignore` includes:
- `.env` (local secrets)
- `.streamlit/secrets.toml` (local secrets)

✅ These are already configured in your project.

## Step 2: Create Streamlit Account

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **"Sign up"**
3. Choose **"Sign up with GitHub"**
4. Authorize Streamlit to access your GitHub account
5. Click **"Continue"**

## Step 3: Deploy Your App

### Option A: Deploy from GitHub (Recommended)

1. Log in to [Streamlit Cloud](https://share.streamlit.io)
2. Click **"New app"**
3. Select:
   - **Repository:** `adeelciit786-hue/bank`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
4. Click **"Deploy!"**

### Option B: Deploy from CLI (Advanced)

```powershell
# Install streamlit CLI
pip install streamlit

# Deploy from your project directory
streamlit run streamlit_app.py
```

Then follow the prompts to deploy.

## Step 4: Configure API Key on Streamlit Cloud

1. Go to your deployed app URL
2. Click the **"☰" menu** (top right)
3. Select **"Settings"**
4. Click **"Secrets"** in the left sidebar
5. Add your API key exactly as shown:
   ```
   MISTRAL_API_KEY = "3Gvc8k5dxnRxSNa2l9PsyWYpYkyCiRhI"
   ```
6. Click **"Save"**

**⚠️ Security:** Streamlit Cloud secrets are encrypted and secure. Your API key is never exposed in code or logs.

## Step 5: Your App is Live!

- Your app URL will be: `https://bank-<random-string>.streamlit.app`
- The app will auto-redeploy whenever you push changes to GitHub
- Share the link with anyone to use your banking assistant

## Local Testing with Streamlit

Before deploying, test locally:

```powershell
# Install streamlit
pip install streamlit

# Run the app
streamlit run streamlit_app.py
```

Access it at: `http://localhost:8501`

## Environment Setup for Local Testing

Create `.streamlit/secrets.toml`:
```toml
MISTRAL_API_KEY = "your_api_key_here"
```

**Don't forget:** This file is in `.gitignore` and won't be pushed to GitHub.

## Troubleshooting

### "MISTRAL_API_KEY not found" Error
- Check that secrets are configured in Streamlit Cloud dashboard
- For local testing, verify `.streamlit/secrets.toml` exists
- Restart the app after adding secrets

### "Cannot import name 'Mistral'" Error
- Requirements.txt is automatically installed by Streamlit
- Run `pip install -r requirements.txt` locally if needed

### "Connection refused" Error
- Check your API key is valid
- Verify internet connection
- Check Mistral API status at https://status.mistral.ai

## Features

✓ Chat interface with message history
✓ Real-time responses from Mistral Large
✓ Security-focused banking assistance
✓ Mobile responsive
✓ Auto-saves conversation
✓ One-click clear history
✓ Professional UI with Streamlit

## Next Steps

1. ✅ Code is ready (you're here!)
2. 📝 Create Streamlit account
3. 🚀 Deploy to Streamlit Cloud
4. 🔑 Add API key to secrets
5. 🎉 Share your banking bot!

## Support

- **Streamlit Docs:** https://docs.streamlit.io
- **Streamlit Community:** https://discuss.streamlit.io
- **Mistral Docs:** https://docs.mistral.ai
- **Your Repo:** https://github.com/adeelciit786-hue/bank

---

**Pro Tip:** Streamlit Cloud offers free hosting with:
- Auto-SSL certificates
- Custom domain support (paid)
- Automatic GitHub integration
- No credit card required for public apps
