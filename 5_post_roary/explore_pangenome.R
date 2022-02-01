library(readr)
library(dplyr)
library(stringr)

data <- read_csv("gene_presence_absence.csv")
unique_genes <- data %>% filter(!is.na(prokka_AZUL) & 
                                  `No. isolates` == 1 & 
                                  Annotation != "hypothetical protein" &
                                  !is.na(`Gene`)) %>% 
  select(c(`Gene`,Annotation))     

shared_with_nearliest <- data %>% filter(!is.na(prokka_AZUL) & 
                                           !is.na(prokka_Rhodopseudomonas_sp._AAP120) & 
                                           `No. isolates` == 2 &
                                           Annotation != "hypothetical protein" &
                                           !is.na(`Gene`)) %>% 
  select(c(`Gene`,Annotation)) 


getGenesByName <- function(string) {
  temp_data <- data %>% mutate(isInAzul = !is.na(prokka_AZUL))  %>% 
    filter(str_detect(`Gene`, string) & 
             Annotation != "hypothetical protein" &
             !is.na(`Gene`)) %>% 
    arrange(`Gene`) %>% 
    select(c(isInAzul,`Gene`,Annotation,`No. isolates`))
}

acr <- getGenesByName("^acr")
actP <-getGenesByName("actP")
ars <- getGenesByName("^ars")
chr <- getGenesByName("^chr")
cop <- getGenesByName("^cop")
cus <- getGenesByName("^cus")
czc <- getGenesByName("^czc")
cnr <- getGenesByName("^cnr")
mer <- getGenesByName("^mer")
znt <- getGenesByName("^znt")

