from django.utils.html import format_html


def create_rel_link(url, label, icon='fa fa-link'):
    return format_html(f"""
    <a class="link-primary" href="{url}">
        <i class="{icon}"></i>
        <u>{label}</u>
    </a>
    """, url=url, label=label)
