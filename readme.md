# CADD-browserTracks

This repository contains the `hub.txt` that provides UCSC genome browser tracks
for [CADD](https://cadd.gs.washington.edu/) versions 1.3 to 1.5.

## Usage

To view the tracks in UCSC genome browser, you need to link to `hub.txt`,
i.e by clicking
[this link](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&hubUrl=https://krishna.gs.washington.edu/download/CADD/bigWig/CADD-browserTracks/hub.txt)
for hg19/GRCh37 and 
[this link](https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&hubUrl=https://krishna.gs.washington.edu/download/CADD/bigWig/CADD-browserTracks/hub.txt)
for hg38/GRCh38.

## About this track

This is a [UCSC genome browser](https://genome.ucsc.edu/cgi-bin/hgGateway)
track [hub](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html).

It displayes the highest CADD score of any 3 possible SNVs for each position.
It is available for every determined genome position (i.e. non-N bases) on the major chromosomes in the reference genome.

The bigWig datasets that are displayed in the tracks are located [on our webserver](https://krishna.gs.washington.edu/download/CADD/bigWig/).

## About CADD

CADD (short for Combined Annotation Dependent Depletion) is a tool for scoring
the deleteriousness of single nucleotide variants as well as
insertion/deletions variants in the human genome
(currently supported builds: GRCh37/hg19 and GRCh38/hg38).

Details about CADD, including features in the latest version, the different
genome builds and how we envision the use case of CADD are described in our
latest manuscript:
<blockquote>
Rentzsch P, Witten D, Cooper GM, Shendure J, Kircher M. <br>
<i>CADD: predicting the deleteriousness of variants throughout the human genome.</i><br>
Nucleic Acids Res. 2018 Oct 29. doi: <a target="_blank" href="http://dx.doi.org/10.1093/nar/gky1016">10.1093/nar/gky1016</a>.<br>
PubMed PMID: <a target="_blank" href="http://www.ncbi.nlm.nih.gov/pubmed/30371827">30371827</a>.
</blockquote>

The original manuscript describing the method and its features was published by Nature Genetics in 2014:
<blockquote>
Kircher M, Witten DM, Jain P, O'Roak BJ, Cooper GM, Shendure J. <br>
<i>A general framework for estimating the relative pathogenicity of human genetic variants.</i><br>
Nat Genet. 2014 Feb 2. doi: <a target="_blank" href="http://dx.doi.org/10.1038/ng.2892">10.1038/ng.2892</a>.<br>
PubMed PMID: <a target="_blank" href="http://www.ncbi.nlm.nih.gov/pubmed/24487276">24487276</a>.
</blockquote>

We provide pre-computed CADD-based scores (C-scores) for all 8.6 billion
possible single nucleotide variants (SNVs) of the reference genome, as well as
all SNV and insertions/deletions variants (InDels) from population-wide whole
genome variant releases and enable scoring of short InDels on our website or 
using an offline script installation.

For updates and further information, please check our
[website](https://cadd.gs.washington.edu)

## Copyright

Copyright (c) University of Washington, Hudson-Alpha Institute for
Biotechnology and Berlin Institute of Health 2013-2019. All rights reserved.

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
