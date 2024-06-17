# 범수쌤 KOGES QC script
# 수정사항
#   1. sexcheck 파일 직접 input으로 받게


library(data.table)
library(ggplot2)

# pref = "KCHIP.abc.snp"
args <- commandArgs(TRUE)

f <- args[1] # sexcheck without pruning
f2 <- args[2] # sexcheck with pruning

# f = sprintf("summary/%s.1.unrelated.mind.rmhet.sexcheck", pref)
# f2 = paste0(strsplit(f, ".sexcheck")[[1]], ".pruned.sexcheck")

# read
df <- fread(f, data.table=FALSE)
df2 <- fread(f2, data.table=FALSE)
# extract
df <- df[df$STATUS=="PROBLEM", ]
df2 <- df2[df2$STATUS=="PROBLEM", ]
df$random <- runif(nrow(df))
df2 <- merge(df2, df[, c("FID", "IID", "random")], by=c("FID", "IID"), all.x=TRUE)

# function: plotting and summary
sexplot <- function(df, fname, pruned=FALSE){
  message(paste0("PROBLEM: ", nrow(df)))
  message(paste0("male: ", nrow(df[df$PEDSEX=="1", ])))
  message(paste0("female: ", nrow(df[df$PEDSEX=="2", ])))
  
  p <- ggplot(data=df) +
    geom_jitter(aes(x=F, y=random, color=factor(PEDSEX)), size=2) +
    geom_vline(xintercept=c(0.2, 0.8), color="red") +
    ylim(0,1) +
    theme(axis.title = element_text(size=15),
          axis.text = element_text(size=13))
  
  ggsave(p, file=paste0(fname, ".problem.png"), width=25, height=25, units="cm")
  
  tblpref = ifelse(pruned==TRUE, "sexcheck.pruned", "sexcheck")
  write.table(df[, c("FID","IID")], file=paste0(tblpref, ".problem"), sep="\t", row.names=FALSE, col.names=FALSE, quote=FALSE, fileEncoding="ascii")
  write.table(df[, 1:(ncol(df)-1)], file=paste0(tblpref, ".problem.detail"), sep="\t", row.names=FALSE, quote=FALSE, fileEncoding="ascii")
}

# run
message("-----> All <-----")
sexplot(df, fname=f)
message("-----> Pruned <-----")
sexplot(df2, fname=f2, pruned=TRUE)

