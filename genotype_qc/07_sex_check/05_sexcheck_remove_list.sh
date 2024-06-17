#!/bin/bash
# Male (F<0.625) and female (F>0.375) in pruned results were removed

echo "Remove individuals"
awk 'BEGIN{FS="\t";OFS="\t"}{if($3==1 && $6<0.625) print $1,$2}' sexcheck.pruned.problem.detail > sexcheck.pruned.rmlist.male
echo "Male: $(wc -l sexcheck.pruned.rmlist.male)"
awk 'BEGIN{FS="\t";OFS="\t"}{if($3==2 && $6>0.375) print $1,$2}' sexcheck.pruned.problem.detail > sexcheck.pruned.rmlist.female
echo "Female: $(wc -l sexcheck.pruned.rmlist.female)"
cat sexcheck.pruned.rmlist.male sexcheck.pruned.rmlist.female > sexcheck.pruned.rmlist
echo ""
