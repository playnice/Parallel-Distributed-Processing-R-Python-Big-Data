#!/usr/bin/env Rscript

library("XML")
library("optparse")
library("tictoc")

globalStartTime = tic(quiet = TRUE)
globalStartTime = toc(quiet = TRUE)

#EVENT HANDLER
startElement = function(name, attrs, .state)  {
  if(name == "row"){
    .state = .state + 1
  }
  if(.state%%1000000 == 0){
    temp <- tic(quiet = TRUE)
    temp <- toc(quiet = TRUE)
    timer <- temp$toc - globalStartTime$tic
    cat("ROW NUMBER PROCESSED: ", .state , "\n")
    cat("Now time at: ", format(Sys.time(), "%F %R:%S")
        , "at" ,timer,"\n\n")
    tic(quiet = TRUE)
  }
  .state
};

#ARGUMENTS TO SET FILEPATH
#REFERENCED FROM
#https://www.r-bloggers.com/passing-arguments-to-an-r-script-from-command-lines/
option_list = list(
  make_option(c("-f", "--file"), type="character", default=NULL, 
              help="dataset file name", metavar="character")
); 

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);
if (is.null(opt$file)){
  print_help(opt_parser)
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

#MAIN PROGRAM
#READ FILENAME FROM USER INPUT IN COMMAND LINE
fileName <- opt$file
cat("PROGRAM STARTING AT: ", format(Sys.time(), "%F %T"),"\n\n")
cat("PARSING ",fileName, "\n\n")

#START SAX PARSING HERE
parser <-xmlEventParse(fileName, handlers = list(startElement = startElement), state = 0)

endTime <- toc(quiet = TRUE)
endTime <- endTime$toc - globalStartTime$tic
cat("TOTAL ROW PARSED: ",parser,"\n\n")
cat("PROGRAM FINISHED AT: ", format(Sys.time(), "%F %T"), "at" ,endTime,"seconds\n")
