#!/usr/bin/bash
iterator=1
url="http://www.deeplearningbook.org/contents/"
array=(
   TOC.html
   acknowledgements.html
   notation.html
   intro.html
   part_basics.html 
   linear_algebra.html
   prob.html
   numerical.html
   ml.html
   part_practical.html
   mlp.html
   regularization.html
   optimization.html
   convnets.html
   rnn.html
   guidelines.html
   applications.html
   part_research.html
   linear_factors.html
   autoencoders.html
   representation.html
   graphical_models.html
   monte_carlo.html 
   partition.html
   inference.html
   generative_models.html
   bib.html
   index-.html
)

echo "Deep learning book downloader"

mkdir -p deeplearningbook
cd deeplearningbook

for filename in "${array[@]}"
do
   echo "==> Downloading from" $url$filename
   wget $url$filename "-O" $iterator"-"$filename
   let iterator+=1
done

cd ..
echo "==> Done, please check the files in "$(pwd)"/deeplearningbook"
