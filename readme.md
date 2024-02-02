# CADD-browserTracks

This repository contains the `hub.txt` that provides genome browser tracks
for [CADD](https://cadd.gs.washington.edu/) versions 1.3 to 1.7 in UCSC genome browser,
NCBI Genome Data Viewer and Ensembl genome browser.

## Usage

To view the tracks in **UCSC genome browser**, you need to link to `hub.txt`,
i.e by clicking
[this link](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&hubUrl=https://kircherlab.bihealth.org/download/CADD/bigWig/CADD-browserTracks/hub.txt)
for hg19/GRCh37 and 
[this link](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&hubUrl=https://kircherlab.bihealth.org/download/CADD/bigWig/CADD-browserTracks/hub.txt)
for hg38/GRCh38.

**NCBI GDV**:
[hg19/GRCh37](https://www.ncbi.nlm.nih.gov/genome/gdv/browser/genome/?acc=GCA_000001405.1&hub=https://kircherlab.bihealth.org/download/CADD/bigWig/CADD-browserTracks/hub.txt)
and
[hg38/GRCh38](https://www.ncbi.nlm.nih.gov/genome/gdv/browser/genome/?acc=GCA_000001405.24&hub=https://kircherlab.bihealth.org/download/CADD/bigWig/CADD-browserTracks/hub.txt)

**Ensembl**:
[hg19/GRCh37](https://grch37.ensembl.org/TrackHub?url=https://kircherlab.bihealth.org/download/CADD/bigWig/CADD-browserTracks/hub.txt;species=Homo_sapiens;name=CADD;registry=1)
and
[hg38/GRCh38](https://www.ensembl.org/TrackHub?url=https://kircherlab.bihealth.org/download/CADD/bigWig/CADD-browserTracks/hub.txt;species=Homo_sapiens;name=CADD;registry=1).
Please note that we have had trouble with Ensembl (no option for older CADD releases) and
you may need to open the above links twice before Ensembl genome browser registers the track.

## About this track

This is a track [hub](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html) for
[UCSC genome browser](https://genome.ucsc.edu/cgi-bin/hgGateway),
[NCBI Genome Data Viewer](https://www.ncbi.nlm.nih.gov/genome/gdv/)
and [Ensembl genome viewer](http://www.ensembl.org).

It displayes the highest CADD score of any 3 possible SNVs for each position.
It is available for every determined genome position (i.e. non-N bases) on the major chromosomes in the reference genome.

The bigWig datasets that are displayed in the tracks are located [on our webserver](https://kircherlab.bihealth.org/download/CADD/bigWig/).

## About CADD

CADD (short for Combined Annotation Dependent Depletion) is a tool for scoring
the deleteriousness of single nucleotide variants, multi-nucleotide substitutions as well as
insertion/deletions variants in the human genome
(currently supported builds: GRCh37/hg19 and GRCh38/hg38).

While many variant annotation and scoring tools are around, most annotations
tend to exploit a single information type (e.g. conservation) and/or
are restricted in scope (e.g. to missense changes). Thus, a broadly applicable metric
that objectively weights and integrates diverse information is needed.
Combined Annotation Dependent Depletion (CADD) is a framework that
integrates multiple annotations into one metric by contrasting variants that
survived natural selection with simulated mutations.

CADD can quantitatively prioritize functional, deleterious, and disease causal
variants across a wide range of functional categories, effect sizes and genetic
architectures and can be used prioritize causal variation in
both research and clinical settings.

CADD has been described in four publications. The most recent manuscript 
describes CADD v1.7, an extension to the annotations included in the model. 
Most prominently, this version improves the scoring of coding variants with 
features derived from the ESM-1v protein language model as well as the 
scoring of regulatory variants with features derived from a convolutional 
neural network trained on regions of open chromatin:

<blockquote>
  Schubach M, Maass T, Nazaretyan L, R&ouml;ner S, Kircher M. <br>
  <i>CADD v1.7: Using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide
    variant predictions.</i><br>
  Nucleic Acids Res. 2024 Jan 5. doi: <a target="_blank"
    href="https://doi.org/10.1093/nar/gkad989">10.1093/nar/gkad989</a>.<br>
    PubMed PMID: <a target="_blank" href="https://pubmed.ncbi.nlm.nih.gov/38183205/">38183205</a>.
</blockquote>

Then there is CADD-Splice (CADD v1.6), which specifically improved the prediction of splicing effects:
<blockquote>
  Rentzsch P, Schubach M, Shendure J, Kircher M. <br>
  <i>CADD-Splice<E2><80><94>improving genome-wide variant effect prediction using deep learning-derived splice scores.</i><br>
  Genome Med. 2021 Feb 22. doi: <a target="_blank"
    href="https://doi.org/10.1186/s13073-021-00835-9">10.1186/s13073-021-00835-9</a>.<br>
  PubMed PMID: <a target="_blank" href="http://www.ncbi.nlm.nih.gov/pubmed/33618777">33618777</a>.
</blockquote>

Our third manuscript describes the updates between the initial publication and CADD v1.4, introduces CADD for GRCh38
and explains how we envision the use of CADD. It was published by Nucleic Acids Research in 2018:
<blockquote>
  Rentzsch P, Witten D, Cooper GM, Shendure J, Kircher M. <br>
  <i>CADD: predicting the deleteriousness of variants throughout the human genome.</i><br>
  Nucleic Acids Res. 2018 Oct 29. doi: <a target="_blank"
    href="http://dx.doi.org/10.1093/nar/gky1016">10.1093/nar/gky1016</a>.<br>
  PubMed PMID: <a target="_blank" href="http://www.ncbi.nlm.nih.gov/pubmed/30371827">30371827</a>.
</blockquote>

Finally, the original manuscript describing the method was published by Nature Genetics in 2014:

<blockquote>
  Kircher M, Witten DM, Jain P, O'Roak BJ, Cooper GM, Shendure J. <br>
  <i>A general framework for estimating the relative pathogenicity of human genetic variants.</i><br>
  Nat Genet. 2014 Feb 2. doi: <a target="_blank" href="http://dx.doi.org/10.1038/ng.2892">10.1038/ng.2892</a>.<br>
  PubMed PMID: <a target="_blank" href="http://www.ncbi.nlm.nih.gov/pubmed/24487276">24487276</a>.
</blockquote>
</p>

For updates and further information, please check our
[website](https://cadd.gs.washington.edu)
or 
[website](https://cadd.bihealth.org)

## Copyright

Copyright (c) University of Washington, Hudson-Alpha Institute for
Biotechnology and Berlin Institute of Health at Charite -- 
Universitaetsmedizin Berlin 2013-2023. All rights reserved.

Permission is hereby granted, to all non-commercial users and licensees of CADD
(Combined Annotation Dependent Framework, licensed by the University of
Washington) to obtain copies of this software and associated documentation
files (the "Software"), to use the Software without restriction, including
rights to use, copy, modify, merge, and distribute copies of the Software. The
above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
