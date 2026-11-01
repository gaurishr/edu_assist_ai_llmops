# OpenAI API Key Setup Guide

## Quick Summary

To use the MLOps Assignment 2 project, you need an OpenAI API key. Here's how to get one:

### 3 Simple Steps:

1. **Sign up/Login**: Go to https://platform.openai.com/
2. **Get API Key**: Navigate to https://platform.openai.com/account/api-keys
3. **Create New Secret Key**: Click "Create new secret key" and copy it

---

## Detailed Setup Instructions

### Step 1: Create OpenAI Account (if you don't have one)

**Website**: https://platform.openai.com/signup

**Requirements**:
- Email address
- Phone number (for verification via SMS)
- Credit/debit card (for billing)
- Valid payment method

**Process**:
1. Click "Sign up"
2. Enter your email
3. Verify your email address
4. Set a password
5. Add phone number and verify
6. Add payment method (credit/debit card)
7. Confirm and complete setup

### Step 2: Generate API Key

**Website**: https://platform.openai.com/account/api-keys

**Steps**:
1. Sign in to your OpenAI account
2. Click on your profile icon (top right corner)
3. Select "View API keys" or go directly to the URL above
4. Click the "+ Create new secret key" button
5. A new key will appear (looks like: `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)
6. **IMPORTANT**: Copy this key immediately and save it somewhere safe!

**Note**: You will NOT be able to see this key again after closing the dialog. If you lose it, you'll need to generate a new one.

### Step 3: Add Key to Your Project

**In Terminal**:

```bash
cd /Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

cp .env.example .env

# Edit .env file and add your API key
nano .env  # or use your favorite text editor
```

**In .env file**, add:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

**Save the file**.

### Step 4: Configure Billing & Limits (IMPORTANT!)

**Website**: https://platform.openai.com/account/billing/overview

1. **Set up billing**: Add payment method if not already done
2. **Set usage limits**: https://platform.openai.com/account/billing/limits
   - Hard limit: $10 (prevents overspending)
   - Soft limit: $5 (alerts you)

**Cost Estimation**:
- This assignment will cost approximately **$0.05 - $0.20**
- Model: gpt-3.5-turbo (most economical)
- 15 API calls total (5 questions × 3 prompt versions)

### Step 5: Test Your API Key

Run this test script to verify your API key works:

```bash
cd /Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

source venv/bin/activate

python3 << 'EOF'
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env file")
    exit(1)

print(f"✓ API Key loaded: {api_key[:20]}...")

try:
    # Create client
    client = OpenAI(api_key=api_key)
    
    # Test API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello, API works!'"}],
        max_tokens=10
    )
    
    print("✓ API Connection successful!")
    print(f"✓ Response: {response.choices[0].message.content}")
    print(f"✓ Tokens used: {response.usage.total_tokens}")
    print("\n✅ Your API key is working! Ready to run the assignment.")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("\nTroubleshooting:")
    print("1. Check .env file exists in project directory")
    print("2. Verify OPENAI_API_KEY line has no extra spaces")
    print("3. Ensure your API key starts with 'sk-'")
    print("4. Check billing is set up at platform.openai.com/account/billing")
    print("5. Verify account is not suspended")

EOF
```

---

## OpenAI Pricing for This Assignment

### Model: GPT-3.5-turbo

| Type | Price |
|------|-------|
| Input tokens | $0.50 per 1M tokens |
| Output tokens | $1.50 per 1M tokens |

### Estimated Costs

```
API Calls: 15 total
  • 5 academic questions
  • 3 prompt versions each
  • ~100 input tokens per call
  • ~150 output tokens per call

Estimated Total Cost: $0.05 - $0.20

Example Breakdown:
  • Input: (1,500 tokens / 1,000,000) × $0.50 = $0.00075
  • Output: (2,250 tokens / 1,000,000) × $1.50 = $0.003375
  • Total per run: ~$0.004
  • Full assignment: ~$0.06
```

### Monthly Projection

If scaled to 10,000 requests per month:
- **Estimated monthly cost: $50 - $200** (depending on prompt/response length)
- This is factored into Task 2 cost analysis

---

## Security Best Practices

### ✅ DO:

- Keep your API key **private and confidential**
- Store API key in `.env` file **only** (not in Python code)
- `.env` is already in `.gitignore` (won't be committed to git)
- **Set usage limits** at https://platform.openai.com/account/billing/limits
- **Regenerate your key** if you accidentally expose it
- Use **different keys for different projects** when possible
- **Rotate keys periodically** for security

### ❌ DON'T:

- **Share your API key** with anyone
- **Commit .env to git/GitHub** (it's already in .gitignore)
- **Hardcode the key** in Python files
- **Post your key** in forums, chat, or social media
- **Use personal keys** for shared team projects
- **Leave key unattended** in files or terminals

### How to Regenerate If Exposed

1. Go to https://platform.openai.com/account/api-keys
2. Find the exposed key in your list
3. Click the trash/delete icon
4. Create a new secret key
5. Update your `.env` file with the new key

---

## Troubleshooting

### Problem: "Invalid API Key"

**Solution**:
- Check that the key is copied exactly with no extra spaces
- Verify `.env` file format: `OPENAI_API_KEY=sk-...`
- Ensure key starts with `sk-` (not `sk_` or other format)
- Try regenerating a new key at https://platform.openai.com/account/api-keys

### Problem: "Insufficient quota"

**Solution**:
- Add a payment method at: https://platform.openai.com/account/billing
- Verify your card is valid and not declined
- Check you haven't exceeded usage limits
- Free trial credits may have expired

### Problem: "API key expired or revoked"

**Solution**:
- Generate a new API key at: https://platform.openai.com/account/api-keys
- Delete old/unused keys to stay organized
- Update your `.env` file with the new key
- Test with the verification script above

### Problem: "Rate limit exceeded"

**Solution**:
- Wait a few minutes before retrying (already handled in project)
- Project includes 0.5-second delays between requests
- Check your usage at: https://platform.openai.com/account/billing/usage

### Problem: Can't create OpenAI account

**Solution**:
- Use a different email address
- Clear your browser cache and cookies
- Try a different browser
- Verify your email domain isn't blocked
- Check that your country supports OpenAI API

### Problem: Phone verification won't work

**Solution**:
- Ensure your phone number is correct with country code
- Try a different phone number
- Wait a few minutes and retry
- Contact OpenAI support if issue persists

---

## Useful Links

| Resource | URL |
|----------|-----|
| Sign up | https://platform.openai.com/signup |
| Sign in | https://platform.openai.com/login |
| API Keys | https://platform.openai.com/account/api-keys |
| Billing | https://platform.openai.com/account/billing/overview |
| Usage | https://platform.openai.com/account/billing/usage |
| Limits | https://platform.openai.com/account/billing/limits |
| API Docs | https://platform.openai.com/docs |
| Pricing | https://openai.com/pricing |
| Status | https://status.openai.com |

---

## Running Your Project After Setup

Once your API key is configured:

```bash
cd /Users/gauri.shanker/Learnings/Assignments/MLOPS/edu_assist_ai_llmops

# Activate virtual environment
source venv/bin/activate

# Start Jupyter
jupyter notebook llmops_assignment.ipynb

# In another terminal, start MLflow UI
mlflow ui --port 5000

# Then open http://localhost:5000 in your browser
```

---

## Complete Checklist

- [ ] Create OpenAI account at https://platform.openai.com/signup
- [ ] Verify email address
- [ ] Add and verify phone number
- [ ] Add payment method (credit/debit card)
- [ ] Generate API key at https://platform.openai.com/account/api-keys
- [ ] Copy and save your API key
- [ ] Create `.env` file: `cp .env.example .env`
- [ ] Add `OPENAI_API_KEY=sk-...` to `.env`
- [ ] Set usage limits at https://platform.openai.com/account/billing/limits
- [ ] Test API key with verification script
- [ ] Run Jupyter notebook: `jupyter notebook llmops_assignment.ipynb`
- [ ] Execute assignment cells
- [ ] View results at `mlflow ui --port 5000`

---

## Questions?

For more information:
- Check the **README.md** in your project
- Review **ASSIGNMENT_INSTRUCTIONS.md**
- Read **DELIVERABLES.md** for implementation details
- Visit OpenAI documentation: https://platform.openai.com/docs

---

**Status**: ✅ Ready to use after adding your API key!

**Cost**: Only $0.05-$0.20 for this entire assignment!

**Next Step**: Get your API key and run the Jupyter notebook!
