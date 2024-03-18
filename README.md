This repository is for my personal files created for larger project looking into the association of antimicrobial resistance (AMR) genes and virulence factors (VFs) on single-replicon IncF plasmids, from a publicly available database, Plasmid Database (PLSDB). 

The main repositoty is availale at https://github.com/frarrivetti/plasmid_side_project/tree/main

**	1. Download plasmid assemblies ** 
- The PLSDB database (Galata et al., 2018, https://ccb-microbe.cs.uni-saarland.de/plsdb/plasmids/) was searched for IncF plasmids (>25 kbp (de Toro et al., 2014) and contains IncF in plasmidfinder field), and fasta sequences downloaded along with .tsv files of metadata.
 
**	2. Filter and organise plasmids **
- The R script PLSDB_filtering.R filters plasmids that are single replicon, circular, and >33kbp to include the minimum size of essential conjugation machinery (Frost et al., 1994), and produces a text file of accession numbers for each plasmid family with >200 members.
- splitAssemblies.py separates the multi-sequence FASTA file downloaded form PLSDB into separate FASTA files for each plasmid and organises them into folders by plasmid family identified above.
 
**	3. ggCaller **
- ggCaller was installed and run on each plasmid family separately with default parameters in Docker, as suggested by the developers (https://ggcaller.readthedocs.io/en/latest/).
- Docker Desktop for Windows was installed (https://docs.docker.com/get-docker/), for use with WSL to run the main analysis, as suggested by ggCaller developers.
- The docker image was built locally after cloning the original github repo using:
  ```
  git clone --recursive https://github.com/samhorsfield96/ggCaller && cd ggCaller
  docker build -t ggc_env:latest -f docker/Dockerfile
  ```
- This step combines gene annotation with creating a pangenome phylogeny using Prokka, as well as other descriptive summaries of gene distribution, into a single workflow.
  
**  4. Coinfinder **
- Coinfinder was installed and run according to developer recommendations (https://github.com/fwhelan/coinfinder) to look for gene association-avoidance patterns. The gene presence-absence matrices and phylogeny inputs were derived from the ggCaller outputs above.



**References:**
de Toro, M., Garcillaon-Barcia, M. P., & De La Cruz, F. (2014). Plasmid Diversity and Adaptation Analyzed by Massive Sequencing of Escherichia coli Plasmids. Microbiol Spectr, 2(6). https://doi.org/10.1128/microbiolspec.PLAS-0031-2014 

Schmartz, G. P., Hartung, A., Hirsch, P., Kern, F., Fehlmann, T., Muller, R., & Keller, A. (2022). PLSDB: advancing a comprehensive database of bacterial plasmids. Nucleic Acids Res, 50(D1), D273-D278. https://doi.org/10.1093/nar/gkab1111 

Galata, V., Fehlmann, T., Backes, C., & Keller, A. (2019). PLSDB: a resource of complete bacterial plasmids. Nucleic Acids Res, 47(D1), D195-D202. https://doi.org/10.1093/nar/gky1050 

Frost, L. S., Ippen-Ihler, K., & Skurray, R. A. (1994). Analysis of the Sequence and Gene Products of the Transfer Region of the F Sex Factor. Microbiological Reviews, 58(2), 162-210. https://doi.org/0146-0749/94/$04.00+0 

Hall, R. J., Whelan, F. J., Cummins, E. A., Connor, C., McNally, A., & McInerney, J. O. (2021). Gene-gene relationships in an Escherichia coli accessory genome are linked to function and mobility. Microb Genom, 7(9). https://doi.org/10.1099/mgen.0.000650 

Whelan, F. J., Rusilowicz, M., & McInerney, J. O. (2020). Coinfinder: detecting significant associations and dissociations in pangenomes. Microb Genom, 6(3). https://doi.org/10.1099/mgen.0.000338 





