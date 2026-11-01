# Getting Your OpenAI API Key

This guide walks you through getting an OpenAI API key and setting it up for this project.

## What's an API Key?

An API key is like a password that lets your code talk to OpenAI's servers. It's how the system knows it's you making requests and can bill you correctly for the API calls you make.

You need this key to run the latency and cost measurement tasks in the assignment.

## Step 1: Create an OpenAI Account (If You Don't Have One)

Go to https://platform.openai.com

Click "Sign up" in the top right corner.

You can sign up with email, Google, Microsoft, or Apple account.

Fill in your information and verify your email address.

Once you're signed up, you'll be taken to the dashboard.

## Step 2: Navigate to API Keys

After you're logged in, go to https://platform.openai.com/account/api-keys

Or click your name in the top right corner, select "Account", then go to "API keys" in the left menu.

You should see a page that says "API keys" at the top.

## Step 3: Create a New API Key

Click the "+ Create new secret key" button.

A modal dialog appears with your new API key.

The key looks like: `sk-proj-abc123def456...`

**Important:** Copy this key immediately. OpenAI only shows it once. If you close the dialog without copying it, you'll need to create a new key.

Copy the entire key to your clipboard.

## Step 4: Add the Key to Your .env File

In your project directory, open the .env file with a text editor:

On macOS:
```bash
open .env
```

On Rocky Linux:
```bash
nano .env
```

Find the line that says:
```
OPENAI_API_KEY=
```

Paste your key after the equals sign. It should look like:
```
OPENAI_API_KEY=sk-proj-abc123def456...
```

Make sure there are no spaces or quotes around the key.

Save the file.

On Rocky Linux with nano: Press Ctrl+X, then Y, then Enter

On macOS: Use Cmd+S in your text editor

## Step 5: Verify It Works

Test that your key is set up correctly:

```bash
python3 << 'VERIFY'
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-'):
    print("✓ API key is set correctly")
    print(f"  Key starts with: {api_key[:10]}...")
else:
    print("✗ API key is not set or invalid")
    print(f"  Check your .env file")
VERIFY
```

If you see the checkmark, you're all set!

## Important Security Notes

**Never commit your API key to git:**
Your .env file is in .gitignore, which means it doesn't get committed. That's intentional. Your API key is private.

**Keep your key secret:**
Don't share your API key with anyone. Don't post it in messages, documents, or code. If you accidentally commit it, regenerate the key immediately.

**Be aware of costs:**
Each API call costs money. The cost depends on how many tokens you use. Monitor your usage in the OpenAI dashboard to avoid surprise bills.

Check your usage here: https://platform.openai.com/account/billing/overview

## Setting Spending Limits

You can set a limit on how much money you'll spend per month:

1. Go to https://platform.openai.com/account/billing/limits
2. Set "Hard limit" to the maximum you want to spend
3. OpenAI will refuse requests once you hit this limit

This is a good safety precaution.

## If Your Key Stops Working

API keys can expire or be disabled. If you get an authentication error:

1. Go to https://platform.openai.com/account/api-keys
2. Check if your key is still listed
3. If not, click "+ Create new secret key" to make a new one
4. Update your .env file with the new key
5. Test it with the verification command above

## If You Have Multiple Projects

You can use the same API key for multiple projects. The .env file in each project just needs to have the same key.

Or you can create different keys for different projects. This helps you track which project is using how much of your API budget.

To view all your keys and how much each has been used:
1. Go to https://platform.openai.com/account/api-keys
2. Each key shows when it was last used

## About API Pricing

The cost of using OpenAI's API depends on which model you're using and how many tokens you use.

This project uses GPT-3.5 or GPT-4 depending on your configuration. Check your config.py to see which model is set.

Token costs as of now:
- GPT-3.5-turbo: About $0.0005 per 1000 input tokens, $0.0015 per 1000 output tokens
- GPT-4: Much more expensive, but more capable

The cost calculation task in the assignment will show you exactly how much each API call costs.

To see current pricing: https://openai.com/pricing

## Alternative: Using Environment Variables

Instead of .env files, you can set the API key as an environment variable:

On macOS:
```bash
export OPENAI_API_KEY=sk-your-key-here
```

On Rocky Linux:
```bash
export OPENAI_API_KEY=sk-your-key-here
```

This works, but the .env file approach is cleaner for a project.

## If the Notebook Says "No API Key"

When you run the notebook, if it says the API key isn't set:

1. Make sure you edited the .env file and added your key
2. Make sure you saved the .env file
3. Restart Jupyter: Close the browser tab, stop the notebook server (Ctrl+C in terminal), then run `jupyter notebook llmops_assignment.ipynb` again
4. Run verify_setup.sh to check

## Help! I Lost My API Key

If you didn't copy your API key before the dialog closed:

1. Go to https://platform.openai.com/account/api-keys
2. Delete the key that you created
3. Click "+ Create new secret key" to make a new one
4. Copy it this time and add it to .env

There's no way to retrieve a lost API key - you have to create a new one.

## Next Steps

Once your API key is set up:

1. Run verify_setup.sh to make sure everything is working
2. Open the Jupyter notebook: jupyter notebook llmops_assignment.ipynb
3. Run the latency and cost cells to start the assignment

You're now ready to use the OpenAI API!
