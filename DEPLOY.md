# Getting this on GitHub Pages

About five minutes, no command line, no Git knowledge needed. You already have a
GitHub account (`docmartin95`), and you will use it — no second login to manage.

## 1. Make a free Organization named `keithjamesii`

This is the step that gets you a clean URL without a second account. GitHub's
terms allow one free personal account per person, but Organizations are free and
unlimited, and an Organization gets its own Pages site at
`<orgname>.github.io` exactly like a personal account does.

So: signed in as `docmartin95`, go to <https://github.com/organizations/plan>,
choose the **Free** plan, and name the organization **`keithjamesii`**. Check
availability first at `github.com/keithjamesii` — a 404 means it's free. If it's
taken, `keithjames2` or `onelandbooks` work the same way; substitute it everywhere
below.

You now own it from your normal login. `docmartin95` stays your code account and
never appears in the author site's address.

## 2. Create the repository inside that organization

1. On the new organization's page, click **New repository**. Check the **Owner**
   dropdown says `keithjamesii`, not `docmartin95` — this is the one place the
   step goes wrong.
2. Repository name: **`keithjamesii.github.io`** — the org name plus `.github.io`.
   That exact name is what puts the site at the root of the address instead of
   down a subfolder.
3. Set it to **Public**. Private repos can't publish free Pages sites.
4. Don't check "Add a README" — this folder already has one.
5. **Create repository**.

## 3. Upload the files

1. On the new empty repo page, click **uploading an existing file**.
2. Unzip the folder I sent, then drag **everything inside it** into the browser
   window — all the files *and* the folders. Not the outer folder itself, its contents.
3. Wait for the upload to finish, then click **Commit changes**.

One thing to watch: `.nojekyll` is invisible in Finder by default. On a Mac,
press **Cmd + Shift + .** in the unzipped folder to reveal hidden files before you
drag. If it doesn't make it up, the site still works — it just builds a bit slower.

## 4. Turn Pages on

1. Repo → **Settings** → **Pages** in the left sidebar.
2. Under "Build and deployment", Source: **Deploy from a branch**.
3. Branch: **main**, folder: **/ (root)**. **Save**.

Give it one to three minutes, then refresh Settings → Pages. A green banner will
show your live link.

## 5. Your URLs

```
https://keithjamesii.github.io/                  home
https://keithjamesii.github.io/kinesthoria       the book
https://keithjamesii.github.io/world             the One Land
https://keithjamesii.github.io/webtoon           adaptation art
https://keithjamesii.github.io/about             bio
https://keithjamesii.github.io/news              updates
https://keithjamesii.github.io/contact           contact + press
```

### If you'd rather skip the organization

Two fallbacks, both fine:

- **Use `docmartin95` directly.** Repo `docmartin95.github.io`, same steps from
  section 3 on. Live in five minutes, and the address reads
  `docmartin95.github.io/kinesthoria`. It also spends your one personal Pages
  site, so a future dev/portfolio page would have to share it.
- **A project repo.** Any repo named, say, `oneland` publishes at
  `docmartin95.github.io/oneland`. The site is built with relative links, so it
  works correctly in a subfolder without any changes.

Either way a custom domain later erases the account name completely, so this
choice is not permanent.

---

## What's on the About page

Per your call, the site now connects Keith James II to James K. Martin II. The
page opens on the pen name and the novel, then moves through the science, the
teaching, and the AI-and-reasoning work, ending with awards and selected
publications. The throughline is that the science explains the fiction — the One
Land runs on physiology, and the novel's question about what a people keep when
their power is taken away is the same question your AI-in-education work asks.

Two things to look at before this goes live:

- **The adjunct title is off the page for now.** The chair has approved it and
  the dean has not, so the site says only "Educational Developer for STEM at the
  Center for Teaching Excellence at The George Washington University," which is
  true today. An HTML comment right above that paragraph in `about/index.html`
  holds the exact replacement sentence; paste it in when the approval lands.
- **The 67 percent figure** for Professor Dobbi stays, per your confirmation.

Everything else on that page is straight from the CV.

## Later: your own domain

If you'd rather have `keithjamesii.com` or `kinesthoria.com` (roughly $12–15 a
year from Cloudflare Registrar, Namecheap, or Porkbun), GitHub Pages supports it
free:

1. Buy the domain.
2. In your registrar's DNS settings, add four `A` records for `@` pointing to
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`,
   and one `CNAME` for `www` pointing to `keithjamesii.github.io`.
3. Repo → Settings → Pages → Custom domain → enter it → Save.
4. Wait for the DNS check to pass, then tick **Enforce HTTPS**.

Existing links keep working; GitHub redirects the `.github.io` address to the new one.

## Updating the site afterward

Open any file on GitHub, click the pencil icon, edit, commit. Live in about a
minute. Search the HTML for `EDIT-ME` — every remaining placeholder is marked.

Still open: the public contact address (currently `hello@example.com`), print buy
links and ISBNs once the listings are live, an opening excerpt for the book page,
and webtoon art for the gallery.
