# CADD-browserTracks

This repository contains the `hub.txt` that provides UCSC genome browser tracks
for [CADD](http://cadd.gs.washington.edu/) versions 1.3 and 1.4

## Usage

To view the tracks in UCSC genome browser we have to link to `hub.txt`,
i.e in case of this repository on GitHub to
http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&hubUrl=https://raw.githubusercontent.com/aerval/CADD-browserTracks/master/hub.txt
for hg19/GRCh37 and
http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&hubUrl=https://raw.githubusercontent.com/aerval/CADD-browserTracks/master/hub.txt
for hg38/GRCh38.

## About this track

This is a [UCSC genome browser](https://genome.ucsc.edu/cgi-bin/hgGateway)
track [hub](https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html)

It displayes the highest CADD score that any of 3 possible SNV at that position has.
It is available for every determined genome position on the major chromosomes in the reference genome.

## About CADD

CADD (short for Combined Annotation Dependent Depletion) is a tool for scoring
the deleteriousness of single nucleotide variants as well as
insertion/deletions variants in the human genome
(currently supported builds: GRCh37/hg19 and GRCh38/hg38).
The manuscript describing the method and its features was published by Nature Genetics in 2014:
*Kircher M, Witten DM, Jain P, O'Roak BJ, Cooper GM, Shendure J. A general framework for estimating the relative pathogenicity of human genetic variants. Nat Genet. 2014 Feb 2.
[doi: 10.1038/ng.2892.](http://dx.doi.org/10.1038/ng.2892) PubMed PMID: 24487276.*

We provide pre-computed CADD-based scores (C-scores) for all 8.6 billion
possible single nucleotide variants (SNVs) of the reference genome, as well as
all SNV and insertions/deletions variants (InDels) from population-wide whole
genome variant releases and enable scoring of short InDels on our website.

For more information, please check our
[website for updates and further information](http://cadd.gs.washington.edu)

## Copyright

Copyright (c) University of Washington, Hudson-Alpha Institute for
Biotechnology and Berlin Institute of Health 2013-2018. All rights reserved.

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
