import re

with open('experience/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything inside <main> except the banner.
# The banner is: <header class="page-banner" style="background-image: url('../assets/banners/Experience.jpeg');"><h1>Experience</h1></header>
# So we can split by this banner, or just use regex.

banner = """<header class="page-banner" style="background-image: url('../assets/banners/Experience.jpeg');"><h1>Experience</h1></header>"""

new_main_content = banner + """
<div class="experience-grid">
  <article>
    <a href="../experience/transcom/"><img src="../assets/transcom-web.jpg" alt="Transcom visit" loading="lazy"></a>
    <h3>Transcom Visit</h3>
  </article>
  <article>
    <a href="../experience/emk/"><img src="../assets/physics-emk-web.jpg" alt="EMK Physics Talk" loading="lazy"></a>
    <h3>EMK Physics Talk</h3>
  </article>
  <article>
    <a href="../experience/bim-conference/"><img src="../assets/bim-conference-web.jpg" alt="BIM Conference Attendance" loading="lazy"></a>
    <h3>BIM Conference Attendance</h3>
  </article>
  <article>
    <a href="../achievements/earth-champions/"><img src="../assets/ecp2022-me-web.jpg" alt="Earth Champions programme" loading="lazy"></a>
    <h3>Earth Champions Programme</h3>
  </article>
  <article>
    <a href="../experience/robotics-demonstration/"><img src="../assets/photo-6172214870665794036-y-web.jpg" alt="Robotics demonstration" loading="lazy"></a>
    <h3>Robotics Demonstration</h3>
  </article>
</div>
"""

# replace everything from <main...> to </main>
# We need to preserve the <main> tag itself.
content = re.sub(r'(<main id="main" class="interior">).*?(</main>)', rf'\1{new_main_content}\2', content, flags=re.DOTALL)

with open('experience/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

