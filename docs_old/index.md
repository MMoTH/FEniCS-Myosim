---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
author_profile: false
layout: single
sidebar:
  nav: "docs"
classes: wide
gallery:

- url: /Projects/threestate_espvr/
  image_path: /assets/images/lvmesh.png
  alt: "Representative LV mesh"
  title: "Featured Projects"
- url: /assets/images/lvmesh.png
  image_path: /assets/images/lvmesh.png
  alt: "Representative LV mesh"
  title: "Featured Projects"
- url: /assets/images/lvmesh.png
  image_path: /assets/images/lvmesh.png
  alt: "Representative LV mesh"
  title: "Featured Projects"
---

<h1><span style="color: #0292ca">M</span><span style="font-weight:normal">ultiscale </span><span style="color: #0292ca">M</span><span style="font-weight:normal">odel </span><span style="color: #0292ca">o</span><span style="font-weight:normal">f </span><span style="color: #0292ca">t</span><span style="font-weight:normal">he </span><span style="color: #0292ca">H</span><span style="font-weight:normal">eart: </span><span style="color: #0292ca">Vent</span><span style="font-weight:normal">ricle Simulations </span></h1>

<!--{% include gallery layout="third"  %}-->

MMotH-Vent is a multi-scale finite-element solver that simulates left ventricular mechanics. Specifically, MMotH-Vent simulates cardiac cycles by coupling a cross-bridge kinetics model to a myocardial tissue constitutive law and circulatory model. More information about each model formulation can be found [here](/MMotH-Vent/model_formulation/model_formulations/).  

MMotH is a collaborative project led by:  
* [Dr. Ken Campbell](https://sites.google.com/g.uky.edu/campbellmusclelab), University of Kentucky
* [Dr. Jonathan Wenk](https://www.engr.uky.edu/directory/wenk-jonathan), University of Kentucky
* [Dr. Lik Chuan Lee](https://researchgroups.msu.edu/compbiomech/), Michigan State University
* [Dr. Chris Yengo](https://sites.psu.edu/yengolab1/), Penn State University

Get started with MMotH-Vent by installing it [here](/MMotH-Vent/getting_started/installation/).

<!--<h3 class="archive__subtitle">{{ site.data.ui-text[site.locale].recent_posts | default: "Recent Posts" }}</h3>-->

<!--{% if paginator %}-->
<!--  {% assign posts = paginator.posts %}-->
<!--{% else %}-->
<!--  {% assign posts = site.posts %}-->
<!--{% endif %}-->

<!--{% for post in posts %}-->
<!--  {% include archive-single.html %}-->
<!--#{% endfor %}-->

<!--{% include paginator.html %}-->
