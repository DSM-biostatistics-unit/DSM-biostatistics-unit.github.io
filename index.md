---
---

# DSM BIOSTATISTICS UNIT

Welcome to the website of the Biostatistics Unit at the Department of Medical, Surgical and Health Sciences, University of Trieste. Here you can learn more about our team, our research, and how to get in touch.


{% include section.html %}


{% capture text %}

Here you can find who's part of the group and what we work on.

{% include button.html
link="team"
text="Meet our team"
icon="fa-solid fa-arrow-right"
flip=true
style="bare"
%}

{% endcapture %}

{% include feature.html
image="images/photo.jpg"
link="team"
title="Our Team"
text=text
%}

{% capture text %}

We focus on statistical methodology applied to health and biomedical data.

{% include button.html
link="research"
text="See our publications"
icon="fa-solid fa-arrow-right"
flip=true
style="bare"
%}

{% endcapture %}

{% include feature.html
image="images/photo.jpg"
link="research"
title="Our Research"
flip=true
style="bare"
text=text
%}
