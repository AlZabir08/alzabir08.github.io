import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """/* Experience Grid */
.experience-section {
    margin-bottom: 50px;
}
.experience-section h2 {
    font-size: 1.5rem;
    margin-bottom: 25px;
    border-bottom: 1px solid var(--line);
    padding-bottom: 10px;
    text-align: center;
}
.experience-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 30px;
}
.experience-grid article {
    text-align: center;
}
.experience-grid img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 8px;
}
@media(max-width: 768px) {
    .experience-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}
@media(max-width: 480px) {
    .experience-grid {
        grid-template-columns: 1fr;
    }
}
"""

css = re.sub(r'/\* Experience Grid \*/.*', new_css, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
