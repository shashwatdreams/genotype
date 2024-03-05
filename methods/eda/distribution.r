library(ggplot2)
library(dplyr)

data <- read.csv('../../data/GT_DataPD_MIT-CS2PD.csv')

data <- select(data, -c(pID, file_1))

ggplot(data, aes(x=gt, fill=gt)) +
  geom_bar() +
  labs(title = "Distribution of People With and Without Parkinson's", x = "Parkinson's Disease", y = "Count") +
  scale_fill_manual(values=c("TRUE"="blue", "FALSE"="red"))

stats_data <- data %>% 
  select(-gt) %>% 
  summarise_all(funs(mean(., na.rm = TRUE))) %>%
  gather(key = "Statistic", value = "Value")

ggplot(stats_data, aes(x = Statistic, y = Value, fill = Statistic)) +
  geom_bar(stat = "identity") +
  labs(title = "Bar Graph of Other Dynamics", x = "Dynamics", y = "Mean Value") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))