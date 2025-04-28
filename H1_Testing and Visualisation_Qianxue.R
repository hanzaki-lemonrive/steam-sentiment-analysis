library(readxl)
library(dplyr)
library(tidyr)
library(writexl)
library(openxlsx)
library(ggplot2)

# Import data
{
  X600coded_processed <- read_excel("600coded_processed.xlsx", 
                                    range = "E1:F360")
}

{
  positivity_table <-  X600coded_processed %>%
    count(Positivity, `Sequel Purchased?`) %>%
    pivot_wider(names_from = `Sequel Purchased?`, values_from = n, values_fill = 0) %>%
    rename(Purchased = `1`, Churned = `0`) %>%
    mutate(Total = Churned + Purchased)
  
  write_xlsx(positivity_table, "positivity_purchase.xlsx")
}

# glm
{
# Fits a regression model
model_H1 <- glm(`Sequel Purchased?` ~ Positivity,
             data = X600coded_processed, family = binomial)

summary(model_H1)

# Count Odds Ratio
intercept_odds <- exp(-0.9429)
positivity_odds <- exp(0.2728)

print(intercept_odds)
print(positivity_odds)

# Calculate 95% CI for OR
exp(confint(model_H1, "(Intercept)"))
exp(confint(model_H1, "Positivity"))
}

# purchase prediction
{
  # Extract model coefficients
  coefficients <- tidy(model)
  print(coefficients)
  
  positivity_new <- data.frame(Positivity = c(0, 1, 2, 3, 4))
  
  positivity_new$Purchased_Probability <- predict(model, newdata = positivity_new, type = "response")
  
  print(positivity_new)
  
  write_xlsx(positivity_new, "Purchase_Predict.xlsx")
}

# visualisation(s)
{
  # import processed data
  positivity_integrated <- read_excel("positivity_integrated.xlsx", 
                                      range = "A1:C6")
  View(positivity_integrated)
  
  # re-arrange the sequence
  ps_long <- ps_long %>%
    arrange(Decision, Positivity)
  
  ps_long <- pivot_longer(
    positivity_integrated,
    cols = c(Churned, Purchased),  # select the columns for transformation
    names_to = "Decision",
    values_to = "Value"
  )
  
  # regression line graph
  ggplot(X600coded_processed, aes(x = Positivity, y = `Sequel Purchased?`)) +
    geom_jitter(width = 0.2, height = 0.05, alpha = 0.3, color = "lightseagreen") +
    stat_smooth(method = "glm", method.args = list(family = "binomial"), 
                se = FALSE, color = "tomato", size = 1.2) +
    labs(title = "Logistic Regression: Positivity vs Sequel Purchase",
         x = "Positivity",
         y = "Probability of Purchasing Sequel") +
    theme_minimal()
  
  # draw a grouped bar chart
ggplot(ps_long, aes(x = Positivity, y = Value, fill = Decision)) +
  geom_bar(stat = "identity", position = "dodge") +  # display in parallel
  labs(title = "Positivity vs Purchase Decision",
       x = "Positivity", y = "Count", fill = "Decision") +
  theme_minimal()

# draw a line chart
ggplot(ps_long, aes(x = Positivity, y = Value, color = Decision, , group = Decision)) +
  geom_line(size = 1) +
  geom_point(size = 3) +
  labs(title = "Positivity vs Purchase Decision",
       x = "Positivity",
       y = "Count",
       color = "Decision") +
  theme_minimal()
}