import re

# 1. Edit certificates/index.html
with open('certificates/index.html', 'r', encoding='utf-8') as f:
    cert_content = f.read()

new_certs = """<article><a class="certificate-image" href="../assets/reviewer-md-basim-al-zabir-shammo.pdf" target="_blank" rel="noopener"><img src="../assets/reviewer-md-basim-al-zabir-shammo-preview.jpg" alt="ICCIT Peer Reviewer certificate" loading="lazy"></a><h2>Peer Reviewer: 28th International Conference On Computer And Information Technology (ICCIT)</h2></article><article><a class="certificate-image" href="../assets/dr-md-basim-al-zabir-shammo.pdf" target="_blank" rel="noopener"><img src="../assets/dr-md-basim-al-zabir-shammo-preview.jpg" alt="RAAICON Peer Reviewer certificate" loading="lazy"></a><h2>Peer Reviewer: 4th IEEE International Conference On Robotics, Automation, Artificial-Intelligence And Internet-Of-Things (RAAICON)</h2></article>"""

cert_content = cert_content.replace('<div class="certificate-grid course-certificates">', f'<div class="certificate-grid course-certificates">{new_certs}')

with open('certificates/index.html', 'w', encoding='utf-8') as f:
    f.write(cert_content)

# 2. Edit experience/index.html
with open('experience/index.html', 'r', encoding='utf-8') as f:
    exp_content = f.read()

# Remove the two View certificate links
exp_content = re.sub(r'<a class="text-link" href="\.\./assets/reviewer-md-basim-al-zabir-shammo\.pdf".*?</a>', '', exp_content)
exp_content = re.sub(r'<a class="text-link" href="\.\./assets/dr-md-basim-al-zabir-shammo\.pdf".*?</a>', '', exp_content)

with open('experience/index.html', 'w', encoding='utf-8') as f:
    f.write(exp_content)

