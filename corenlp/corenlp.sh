#!/usr/bin/env zsh

# usage:
# $ ./corenlp.sh path/to/filelist path/to/outputdir

echo "$( cd -P "$( dirname "$SOURCE" )" && pwd )"

filelist=$1
outputdir=$2

corenlp -props props.properties \
    -filelist ${filelist} \
    -outputDirectory ${outputdir}

# 'corenlp' is alias to java -cp "$CLASSPATH" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
# paths to jar files of corenlp are in "$CLASSPATH"
