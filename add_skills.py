import re

with open('skills/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Microsoft SQL to Programming & modeling
sql_html = '<figure class="skill-logo"><img src="../assets/skills/microsoftsqlserver-original.svg" alt="Microsoft SQL logo" loading="lazy" width="130" height="96"><figcaption>Microsoft SQL</figcaption></figure>'
# Insert after MATLAB (which is the last in Programming & modeling)
content = re.sub(
    r'(<figcaption>MATLAB</figcaption></figure>)',
    rf'\1{sql_html}',
    content
)

# Add Webots and Cisco Packet Tracer to Electronics & simulation
webots_html = '<figure class="skill-logo"><img src="../assets/skills/webots.png" alt="Webots Simulator logo" loading="lazy" width="130" height="96" style="object-fit: contain;"><figcaption>Webots Simulator</figcaption></figure>'
cisco_html = '<figure class="skill-logo"><img src="../assets/skills/cisco.svg" alt="Cisco Packet Tracer logo" loading="lazy" width="130" height="96"><figcaption>Cisco Packet Tracer</figcaption></figure>'

# Insert after Proteus (which is the last in Electronics & simulation)
content = re.sub(
    r'(<figcaption>Proteus</figcaption></figure>)',
    rf'\1{webots_html}{cisco_html}',
    content
)

with open('skills/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

