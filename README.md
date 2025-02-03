<h1 align="center">Atmospheric retrievals using petitRADTRANS</h1>

<p>This project focuses on atmospheric retrievals for a variety of Sub-Neptune exoplanets. Atmospheric retrievals are a powerful method for characterizing exoplanetary atmospheres by inferring their physical properties, chemical abundances, and other characteristics from an observed spectrum.</p>

<p>This repository contains the Jupyter Notebooks I have developed to evaluate different temperature-pressure profiles, chemical abundance models, and cloud/haze properties in the atmospheres of the analyzed planets. Additionally, the repository includes the spectrum data used in the retrievals and some models for the temperature-pressure profile, not included in the built-in models of _petit_, that I have developed and used in the retrievals.</p>

<p>The content of this repository is part of my undergraduate thesis and it is a work in progress. I aim to update it regularly as I continue refining the models and exploring new approaches.</p>

<h2> File descriptions</h2>

<h2>Spectra data</h2>
The data used in the retrievals consists of the transmission spectrum of K2-18b in the range between $0.9 - 5.2 \mu m$, obtained with the NIRISS ($0.9 - 2.8 \mu m$) and NIRSPEC ($2.8 - 5.2 \mu m$) instruments of the JWST. 
The spectrum was reported by <a href="#madhu2023">Madhusudhan et al. (2023)</a> and the high resolution spectrum, along with a low resolution spectrum used for plotting purposes, can be found <a href="https://osf.io/36djh/">here</a>.
<div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
    <img src="./figures/low_res_spectra.png" alt="K2-18b spectrum" width="800">
</div>

<h2>Retrieval setup</h2>

<h2>Temperature-Pressure profiles</h2>

<h2>Chemical models for abundances</h2>

<h2>Clouds and Hazes parameterizations</h2>

<h2>Provitional results and discussion</h2>

<h2>References</h2>
<span id="madhu2023">Madhusudhan N., Sarkar S., Constantinou S., Holmberg M., Piette A. A. A.,
Moses J. I., 2023, Carbon-bearing Molecules in a Possible Hycean Atmosphere (arXiv:2309.05566)</span>
<h2>Acknowledgments</h2>
