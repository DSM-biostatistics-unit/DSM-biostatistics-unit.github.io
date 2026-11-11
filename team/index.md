---
title: Team
nav:
  order: 1
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'member'" %}

## Collaborators

{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'collaborator'" %}

