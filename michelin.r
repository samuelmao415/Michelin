michelin_guide<-read.csv("./michelin/michelin_guide.csv")
#michelin$star <- 
michelin_guide$distinction<-as.character(michelin_guide$distinction)
#michelin_guide$star<-
michelin_guide$star<-gsub("(.*)(Star|Stars) .*", "\\1 \\2", michelin_guide$distinction,perl = TRUE)

michelin_guide$star[!grepl("Star|Stars", michelin_guide$star,perl = TRUE)]<-""

michelin_guide<-michelin_guide%>%select(product_name,star,price,classification,website,distinction,description)

michelin_guide%>% write.csv('./michelin_guide.csv'
                                              , row.names = FALSE
                                              , quote = TRUE)
