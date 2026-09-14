# -*- coding: utf-8 -*-
"""
All site copy lives here. Change text, run `python3 _build.py`, done.
Jacket copy, series name, world terms and author bio are taken verbatim from
the printed paperback and hardcover covers. Anything still marked EDIT-ME is a
placeholder waiting on a decision or a link.
"""

AMAZON = "https://www.amazon.com/dp/B0HHY83GPY"
EMAIL  = "hello@example.com"            # EDIT-ME: the address you want public

LOCKUP = """
<div class="lockup">
  <h1 class="lockup__title">Kinesthoria</h1>
  <hr class="lockup__rule">
  <p class="lockup__sub">The Weight of Wheels</p>
  <p class="lockup__series">A Novel of the One Land</p>
  <p class="lockup__motto">Movement is Life, Motion is Power</p>
</div>
"""

JACKET = """
<p>A century after the drilling catastrophe called the Great Convergence folded the map of the
  world into one wounded landmass, the settlements of the One Land move on muscle, wind and
  hand-brazed steel. Veera hauls sacred oil across the Plain of Memories on a cargo bicycle eight
  times her weight, bred by the gene-readers for lung capacity and nothing else.</p>
<p>When raiders on razor stilts come out of the heat-shimmer, she turns her hauling machine into a
  war-horse, and a Stone-Walker chief names her for it. What he tells her next is worse than the
  raid: something is waking in the northern oil-fields, machines that walk but do not breathe, and
  the only people who can read the pattern are the ones nobody asked.</p>
<p class="close">Kinesthoria is a story about inheritance that testing cannot measure, and about
  what a people keep when everything that made them powerful has been burned.</p>
"""

COVER = ('<div class="cover"><img src="{p}assets/img/cover.jpg" width="1400" height="2104" '
         'alt="Cover of Kinesthoria: The Weight of Wheels &mdash; a rider on a cargo bicycle '
         'crossing a dust plain past a beached ship"></div>')

# ---------------------------------------------------------------- home ------

HOME = """
<section class="hero">
  {spokes}
  <div class="wrap">
    <div class="hero__inner">
      <p class="eyebrow">Keith James II</p>
      """ + LOCKUP + """
      <p class="hook" style="margin-top:.4em">The fuel is gone.<br>The wheels are not.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="{amazon}">Read the book</a>
        <a class="btn btn--ghost" href="{p}world/">Enter the One Land</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="book">
      <div>
        """ + COVER + """
        <ul class="meta">
          <li><span>Series</span><span>A Novel of the One Land</span></li>
          <li><span>Editions</span><span>Hardcover &middot; Paperback &middot; Kindle</span></li>
          <li><span>Genre</span><span>Post-apocalyptic science fiction</span></li>
          <li><span>Published</span><span>2026</span></li>
        </ul>
      </div>
      <div class="jacket">
        <p class="eyebrow">The novel</p>
        <h2 style="margin-bottom:.55em">The Weight of Wheels</h2>
        <hr class="rule-brass">
        """ + JACKET + """
        <div class="btn-row">
          <a class="btn btn--solid" href="{amazon}">Buy on Amazon</a>
          <a class="btn btn--ghost" href="{p}kinesthoria/">Editions &amp; excerpt</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="grid grid--3">
      <a class="card card--link" href="{p}world/">
        <h3>The One Land</h3>
        <p>The Great Convergence, the Plain of Memories, the gene-readers, and what walks in the
          northern oil-fields.</p>
      </a>
      <a class="card card--link" href="{p}webtoon/">
        <h3>The Webtoon</h3>
        <p>He is adapting Kinesthoria into a serialized illustrated edition. Art and progress
          live here.</p>
      </a>
      <a class="card card--link" href="{p}about/">
        <h3>Keith James II</h3>
        <p>Princeton-trained molecular biologist, STEM educational developer, and 2026 New Jersey State Council on the Arts fellow in prose.</p>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow" style="text-align:center">
    <p class="eyebrow">Stay in touch</p>
    <h2>Updates on the book and the adaptation</h2>
    <p class="dim">Occasional notes on the One Land and on the illustrated edition as art comes in.
      A few emails a year.</p>
    <!-- EDIT-ME: paste your Substack / Mailchimp / Buttondown embed in place of this form.
         GitHub Pages is static, so a plain <form> collects nothing on its own. -->
    <form class="field-row" style="justify-content:center" onsubmit="return false">
      <input type="email" placeholder="you@example.com" aria-label="Email address">
      <button class="btn btn--solid" type="submit">Subscribe</button>
    </form>
  </div>
</section>
"""

# --------------------------------------------------------- kinesthoria ------

KINESTHORIA = """
<section class="hero">
  {spokes}
  <div class="wrap">
    <div class="hero__inner" style="padding:80px 0 66px">
      <p class="eyebrow">Book one</p>
      """ + LOCKUP + """
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="book">
      <div>
        """ + COVER + """
        <div class="btn-row" style="flex-direction:column">
          <a class="btn btn--solid" href="{amazon}" style="text-align:center">Kindle edition</a>
          <!-- EDIT-ME: add the hardcover and paperback buy links once the listings are live,
               plus Kobo / Apple Books / Bookshop / library links if you want them. -->
        </div>
        <ul class="meta">
          <li><span>Series</span><span>A Novel of the One Land</span></li>
          <li><span>Editions</span><span>Hardcover, paperback, Kindle</span></li>
          <li><span>Category</span><span>Post-apocalyptic science fiction</span></li>
          <li><span>ASIN</span><span>B0HHY83GPY</span></li>
          <!-- EDIT-ME: add <li><span>ISBN</span><span>...</span></li> for print editions -->
        </ul>
      </div>

      <div class="jacket">
        <p class="hook">The fuel is gone.<br>The wheels are not.</p>
        """ + JACKET + """

        <div style="margin:54px 0 0">
          <blockquote class="pullquote">
            Movement is Life, Motion is Power.
            <cite>The One Land</cite>
          </blockquote>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">Read a piece of it</p>
    <h2>Excerpt</h2>
    <hr class="rule-brass">
    <p class="dim">An opening excerpt goes here.</p>
    <!-- EDIT-ME: paste the opening scene, or the first two pages. An excerpt on the page holds a
         reader better than a link asking them to leave. Delete this whole section until you
         have one. -->
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow">
    <h2>Praise</h2>
    <hr class="rule-brass">
    <p class="dim">Reviews and reader quotes as they come in.</p>
    <!-- EDIT-ME: delete this whole section until you have two or three worth showing. -->
  </div>
</section>
"""

# ---------------------------------------------------------------- world -----

WORLD = """
<section class="section">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">Worldbuilding</p>
    <h1 style="font-size:clamp(2.1rem,5vw,3.2rem)">The One Land</h1>
    <hr class="rule-brass">
    <p class="lede">A century after the Great Convergence, everything that moves in the One Land
      moves because a person spends themselves to move it.</p>
    <p class="dim">These are the terms a reader meets on the jacket, before chapter one.</p>
    <!-- EDIT-ME: expand any entry, and add the ones that only make sense after chapter one. -->
  </div>
</section>

<section class="section section--tight section--alt">
  <div class="wrap wrap--narrow">
    <ul class="termlist">
      <li>
        <p class="term">The Great Convergence</p>
        <p>The drilling catastrophe, roughly a century past, that folded the map of the world into
          one wounded landmass.</p>
      </li>
      <li>
        <p class="term">The One Land</p>
        <p>What was left. Its settlements move on muscle, wind, and hand-brazed steel.</p>
      </li>
      <li>
        <p class="term">The Plain of Memories</p>
        <p>The crossing Veera hauls sacred oil over, on a cargo bicycle carrying eight times
          her weight.</p>
      </li>
      <li>
        <p class="term">The gene-readers</p>
        <p>They bred Veera for lung capacity and nothing else. That is the inheritance testing
          can measure.</p>
      </li>
      <li>
        <p class="term">Raiders on razor stilts</p>
        <p>They come out of the heat-shimmer. Veera turns her hauling machine into a war-horse
          and rides at them.</p>
      </li>
      <li>
        <p class="term">The Stone-Walkers</p>
        <p>One of their chiefs gives Veera a name for what she did in the raid, and then tells her
          something worse.</p>
      </li>
      <li>
        <p class="term">The northern oil-fields</p>
        <p>Something is waking there. Machines that walk but do not breathe, and a pattern only
          the people nobody asked can read.</p>
      </li>
      <!-- EDIT-ME: add regions, guilds, machines, and the handful of invented words a reader
           will want defined. -->
    </ul>
  </div>
</section>
"""

# -------------------------------------------------------------- webtoon -----

WEBTOON = """
<section class="section">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">In development</p>
    <h1 style="font-size:clamp(2.1rem,5vw,3.2rem)">Kinesthoria, illustrated</h1>
    <hr class="rule-brass">
    <p class="lede">He is adapting the novel into a serialized webtoon with a manga- and
      anime-influenced visual language.</p>
    <p class="dim">Concept art, character sheets, and pilot pages appear below as they are
      commissioned.</p>
    <!-- EDIT-ME: drop image files into assets/img/ and replace each .tile div with an <img>. -->
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="gallery">
      <div class="tile">Veera, character sheet</div>
      <div class="tile">Cargo bicycle design</div>
      <div class="tile">Plain of Memories</div>
      <div class="tile">Razor stilts</div>
      <div class="tile">Pilot page 01</div>
      <div class="tile">Pilot page 02</div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap wrap--narrow">
    <h2>Artists</h2>
    <hr class="rule-brass">
    <p>Illustrators interested in the adaptation can write to him. He pays for pilot-chapter
      work and briefs it in advance.</p>
    <div class="btn-row"><a class="btn btn--ghost" href="{p}contact/">Get in touch</a></div>
  </div>
</section>
"""

# ---------------------------------------------------------------- about -----

ABOUT = """
<section class="section">
  <div class="wrap">
    <div class="book">
      <div>
        <div class="cover"><img src="{p}assets/img/author.jpg" width="1000" height="1250"
             alt="Keith James II"></div>
        <ul class="meta">
          <li><span>Writes as</span><span>Keith James II</span></li>
          <li><span>Also</span><span>James K. Martin II, PhD</span></li>
          <li><span>Based in</span><span>Delaware</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">About</p>
        <h1 style="font-size:clamp(2.1rem,5vw,3rem)">Keith James II</h1>
        <hr class="rule-brass">
        <p class="lede">Keith James II is the pen name of James K. Martin II. He trained as a
          molecular biologist and spent years on how cells survive stress. Then he wrote a novel
          about people who haul cargo with their bodies, because nothing else in their world is
          left to do it.</p>
        <p>Kinesthoria: The Weight of Wheels is his first novel of the One Land. He is adapting it
          into an illustrated edition now.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap wrap--narrow">
    <h2>The science underneath</h2>
    <hr class="rule-brass">
    <p>He earned his PhD in molecular biology at Princeton, where his first-author paper in
      <em>Cell</em> described a dual-mechanism antibiotic that kills gram-negative bacteria without
      breeding resistance. At the University of Chicago he moved into cancer biology, running
      genome-wide screens of what a tumor needs when nutrients run short. At a drug-discovery
      startup he built a working microbiology lab out of an empty room.</p>
    <p>The One Land runs on physiology. Lung capacity, load, and the cost of hauling eight times
      your own weight across open ground drive what happens. The gene-readers measure a person the
      way a screen measures a cell line, accurately and for exactly one thing. The novel follows
      what that measurement misses.</p>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow">
    <h2>Teaching</h2>
    <hr class="rule-brass">
    <!-- The adjunct appointment is chair-approved and awaiting the dean. Once it clears, change
         the first sentence to: "He is Educational Developer for STEM at the Center for Teaching
         Excellence at The George Washington University, and an adjunct assistant professor
         there." Nothing else needs to move. -->
    <p>He is Educational Developer for STEM at the Center for Teaching Excellence at The George
      Washington University. He works with faculty in the sciences, engineering, computing, and
      the health professions on course design and assessment.
      Before GW he taught pre-clerkship medical students at Rowan-Virtua School of Osteopathic
      Medicine. He directed a cardiovascular and renal physiology block there, and co-directed a
      program on AI in medicine that reached more than 900 learners a year.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap wrap--narrow">
    <h2>AI, and the reasoning it offers to replace</h2>
    <hr class="rule-brass">
    <p>His current work asks how instructors can use AI without hollowing out the reasoning it is
      meant to support. He leads his center's work on ethical AI integration in STEM instruction,
      and he co-built Professor Dobbi, a domain-constrained Socratic tutor that asks rather than
      answers. In a pilot evaluation it cut D and F rates by 67 percent.</p>
    <p>He has written on information literacy as a shared cognitive architecture, and on what
      medical students lose when a model does the appraisal for them.</p>
    <p>Kinesthoria asks a version of the same question. What does a people keep after the thing that
      made them powerful burns, or gets handed to a machine? In the One Land the engines are gone
      and the reasoning still has to happen.</p>
    <p>He reads and writes the science fiction that keeps its own rules. If a world runs on muscle,
      its characters get tired, and the story has to account for that.</p>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow">
    <h2>Selected recognition</h2>
    <hr class="rule-brass">
    <ul class="termlist">
      <li>
        <p class="term">Individual Artist Fellowship in Prose, 2026</p>
        <p>New Jersey State Council on the Arts, selected from 870 applicants.</p>
      </li>
      <li>
        <p class="term">President&rsquo;s Award for Excellence in Innovative Instructional Delivery, 2026</p>
        <p>Rowan University, with Jeffrey Powers, for Professor Dobbi.</p>
      </li>
      <li>
        <p class="term">Innovation in Medical Education Award, 2026</p>
        <p>AACOM and the Society of Osteopathic Medical Educators, with Jeffrey Powers.</p>
      </li>
      <li>
        <p class="term">Selected publications</p>
        <p>First author, <em>Cell</em> (2020), on a dual-mechanism antibiotic. Medical education
          work in <em>Medical Science Educator</em> and the <em>Journal of the Medical Library
          Association</em>.</p>
      </li>
    </ul>
    <!-- EDIT-ME: add or cut entries here. A reader who came for the novel reads the first two.
         A journalist or a rights editor reads all of them. -->
    <div class="btn-row">
      <a class="btn btn--ghost" href="{p}contact/">Contact &amp; press</a>
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- news -----

NEWS = """
<section class="section">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">Updates</p>
    <h1 style="font-size:clamp(2.1rem,5vw,3.2rem)">News</h1>
    <hr class="rule-brass" style="margin-bottom:44px">
    <ul class="entries">
      <li>
        <time datetime="2026">2026</time>
        <div>
          <h3>Kinesthoria is available in three editions</h3>
          <p>The Weight of Wheels is out in hardcover, paperback, and Kindle.
            <a href="{amazon}">Read it here.</a></p>
        </div>
      </li>
      <li>
        <time datetime="2026">2026</time>
        <div>
          <h3>Fellowship in Prose</h3>
          <p>Named a 2026 Individual Artist Fellow in Prose by the New Jersey State Council on
            the Arts.</p>
        </div>
      </li>
      <li>
        <time datetime="2026">2026</time>
        <div>
          <h3>Illustrated adaptation in development</h3>
          <p>Early art direction underway for a serialized webtoon edition.
            <a href="{p}webtoon/">Follow along.</a></p>
        </div>
      </li>
      <!-- EDIT-ME: newest entries at the top. -->
    </ul>
  </div>
</section>
"""

# -------------------------------------------------------------- contact -----

CONTACT = """
<section class="section">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">Get in touch</p>
    <h1 style="font-size:clamp(2.1rem,5vw,3.2rem)">Contact</h1>
    <hr class="rule-brass">
    <p class="lede">Rights inquiries, interviews, school and library visits, and illustration
      collaborations all reach the same inbox.</p>
    <p><a class="btn btn--solid" href="mailto:EMAIL_HERE">EMAIL_HERE</a></p>
    <!-- EDIT-ME: replace EMAIL_HERE in pages.py with the address you want public.
         A dedicated address is worth setting up rather than a personal one. -->
  </div>
</section>

<section class="section section--tight section--alt">
  <div class="wrap">
    <div class="grid grid--3">
      <div class="card">
        <h3>Press</h3>
        <p>He sends cover files at print resolution, plus an author photo, to anyone covering
          the book.</p>
      </div>
      <div class="card">
        <h3>Rights</h3>
        <p>Translation and audio inquiries reach him directly.</p>
      </div>
      <div class="card">
        <h3>Events</h3>
        <p>He takes classroom visits and panels, in person or remote.</p>
      </div>
    </div>
  </div>
</section>
"""

CONTACT = CONTACT.replace("EMAIL_HERE", EMAIL)

_D = ("Kinesthoria: The Weight of Wheels by Keith James II. A century after the Great Convergence, "
      "the settlements of the One Land move on muscle, wind and hand-brazed steel.")

PAGES = [
    ("",            "Keith James II &mdash; Kinesthoria: The Weight of Wheels", _D, HOME, "website"),
    ("kinesthoria", "Kinesthoria: The Weight of Wheels &mdash; Keith James II",
     _D + " Available in hardcover, paperback, and Kindle.", KINESTHORIA, "book"),
    ("world",       "The One Land &mdash; The world of Kinesthoria",
     "The Great Convergence, the Plain of Memories, the gene-readers, and the machines waking in the northern oil-fields.",
     WORLD, "article"),
    ("webtoon",     "The Kinesthoria Webtoon &mdash; In development",
     "Concept art and progress on the serialized illustrated adaptation of Kinesthoria.",
     WEBTOON, "article"),
    ("about",       "About Keith James II",
     "Keith James II is the pen name of James K. Martin II, a Princeton-trained molecular biologist, STEM educational developer at George Washington University, and 2026 New Jersey fellow in prose.",
     ABOUT, "profile"),
    ("news",        "News &mdash; Keith James II",
     "Releases, awards, and adaptation news from Keith James II.", NEWS, "website"),
    ("contact",     "Contact &amp; Press &mdash; Keith James II",
     "Rights inquiries, interviews, school visits, and illustration collaborations.", CONTACT, "website"),
]
