import re

with open('experience/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

banner = """<header class="page-banner" style="background-image: url('../assets/banners/Experience.jpeg');"><h1>Experience</h1></header>"""

new_content = banner + """
<div class="experience-section">
    <h2>Earth Champions Programme</h2>
    <div class="experience-grid">
        <article><img src="../assets/ecp2022-me-web.jpg" alt="Earth Champions Programme" loading="lazy"></article>
        <article><img src="../assets/ecp2022-team-web.jpg" alt="Earth Champions Programme" loading="lazy"></article>
        <article><img src="../assets/ecp2022-web.jpg" alt="Earth Champions Programme" loading="lazy"></article>
        <article><img src="../assets/ecp-news-paper-web.jpg" alt="Earth Champions Programme" loading="lazy"></article>
        <article><img src="../assets/ecp-2022-web.jpg" alt="Earth Champions Programme" loading="lazy"></article>
        <article><img src="../assets/ecp2022-2-web.jpg" alt="Earth Champions Programme" loading="lazy"></article>
    </div>
</div>

<div class="experience-section">
    <h2>Transcom Visit</h2>
    <div class="experience-grid">
        <article><img src="../assets/transcom-web.jpg" alt="Transcom Visit" loading="lazy"></article>
        <article><img src="../assets/transcom2-web.jpg" alt="Transcom Visit" loading="lazy"></article>
        <article><img src="../assets/transcom3-web.jpg" alt="Transcom Visit" loading="lazy"></article>
    </div>
</div>

<div class="experience-section">
    <h2>EMK Physics Talk</h2>
    <div class="experience-grid">
        <article><img src="../assets/physics-emk-web.jpg" alt="EMK Physics Talk" loading="lazy"></article>
        <article><img src="../assets/physics-emk2-web.jpg" alt="EMK Physics Talk" loading="lazy"></article>
    </div>
</div>

<div class="experience-section">
    <h2>BIM Conference Attendance</h2>
    <div class="experience-grid">
        <article><img src="../assets/bim-conference-web.jpg" alt="BIM Conference Attendance" loading="lazy"></article>
    </div>
</div>

<div class="experience-section">
    <h2>Robotics Demonstration</h2>
    <div class="experience-grid">
        <article><img src="../assets/photo-6172214870665794036-y-web.jpg" alt="Robotics Demonstration" loading="lazy"></article>
    </div>
</div>
"""

# Replace contents inside <main id="main" class="interior">...</main>
content = re.sub(r'(<main id="main" class="interior">).*?(</main>)', rf'\1{new_content}\2', content, flags=re.DOTALL)

with open('experience/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
