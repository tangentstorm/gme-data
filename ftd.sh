#!/bin/sh
# extract GME FTD data from the master SEC files.
# it's just extracting the first header line from one of the sec files,
# and then extracts any lines where the symbol is GME or one of the ETFS
head -1 raw/sec/ftd/cnsfails202101a.txt > gme/ftd.txt
perl -na -F'[|]' -e 'print if $F[2] =~ /^(GME|GAMR|XRT|RETL|XSVM|VIOV|RWJ|VIOO|PSCD|VIOG|VTWV|IUSS|VCR|VTWO|SFYF|IWC|EWSC|SYLD|PRF|RALS|FNDX|FNDB|VBR|IJS|XJR|NUSC|SLYV|IJR|SPSM|SLY|FLQS|IJT|GSSC|SLYG|VXF|NVQ|IWN|ESML|VB|SAA|DMRS|BBSC|OMFS|FDIS|STSB|SSLY|IWM|SCHA|PBSM|UWM|VTHR|URTY|VTI|TILT|VLU|HDG|AVUS|MMTM|DSI|SPTM|IWV|SCHB|ITOT|DFAU)$/' raw/sec/ftd/cnsfails20210* >> gme/ftd.txt

