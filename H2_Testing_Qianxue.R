library(readxl)
library(dplyr)
library(tidyr)
library(writexl)
library(openxlsx)
library(broom)
library(ggplot2)

# Import data
{
coded_sifted <- read_excel("600_codes_only.xlsx",
                           col_types = c("text", "numeric", "numeric", 
                                         "numeric", "numeric", "numeric")
                           )
coded_sifted <- coded_sifted %>%
  filter(!is.na(`Sequel Purchased?`))

write_xlsx(coded_sifted, "600coded_sifted.xlsx")
}

# Gameplay
{
  gameplay_table <- coded_sifted %>%
    count(Gameplay, `Sequel Purchased?`) %>%
    pivot_wider(names_from = `Sequel Purchased?`, values_from = n, values_fill = 0) %>%
    rename(Purchased = `1`, Churned = `0`) %>%
    mutate(
      Total = Churned + Purchased,
      Percentage = paste0(round(Total / 359 * 100, 2), "%"),
      Gameplay = as.character(Gameplay)
    ) %>%
    mutate(
      Gameplay = case_when(  # Rename "0" and "1" 
        Gameplay == 0 ~ "Non-Positive",
        Gameplay == 1 ~ "Positive",
        TRUE ~ Gameplay  # Deal with other possible values
      )
    )
  
  
  # Set summary_row to calculate only numeric variables
  summary_row1 <- gameplay_table %>%
    summarise(across(where(is.numeric), sum)) %>%
    mutate(Gameplay = "Total", Percentage = "100%")
  
  gameplay_table <- bind_rows(gameplay_table, summary_row1)
  gameplay_table

  # chi-squared
  gameplay_chisq <- chisq.test(matrix(c(115, 48, 122, 74), nrow = 2, byrow = TRUE))
  print(gameplay_chisq)
  
gp_long <- data.frame(
  Gameplay = rep(c("Non-Positive", "Positive"), c(163, 196)),
  Purchased = c(rep(0, 115), rep(1, 48), rep(0, 122), rep(1, 74))
)

# Fits a logistic regression model
model <- glm(Purchased ~ Gameplay, data = gp_long, family = binomial)

summary(model)

confint(model)

# Count Odds Ratio
intercept_a_odds <- exp(-0.8737)
gp_1_odds <- exp(0.3738)

print(intercept_a_odds)
print(gp_1_odds)
}

# Storyline
{
storyline_table <- coded_sifted %>%
  count(Storyline, `Sequel Purchased?`) %>%
  pivot_wider(names_from = `Sequel Purchased?`, values_from = n, values_fill = 0) %>%
  rename(Purchased = `1`, Churned = `0`) %>%
  mutate(
    Total = Churned + Purchased,
    Percentage = paste0(round(Total / 359 * 100, 2), "%"),
    Storyline = as.character(Storyline)
  ) %>%
    mutate(
      Storyline = case_when(  # Rename "0" and "1" 
        Storyline == 0 ~ "Non-Positive",
        Storyline == 1 ~ "Positive",
        TRUE ~ Storyline  # Deal with other possible values
      )
    )
  
  # Set summary_row to calculate only numeric variables
  summary_row2 <- storyline_table %>%
    summarise(across(where(is.numeric), sum)) %>%
    mutate(Storyline = "Total", Percentage = "100%")
  
  storyline_table <- bind_rows(storyline_table, summary_row2)
  storyline_table
  
  # 卡方检验
  storyline_chisq <- chisq.test(matrix(c(206, 104, 31, 18), nrow = 2, byrow = TRUE))
  print(storyline_chisq)
  
  sl_long <- data.frame(
    Storyline = rep(c("Non-Positive", "Positive"), c(310, 49)),
    Purchased = c(rep(0, 206), rep(1, 104), rep(0, 31), rep(1, 18))
  )
  
  # Fits a logistic regression model
  model <- glm(Purchased ~ Storyline, data = sl_long, family = binomial)
  
  summary(model)
  
  confint(model)
  
  # Count Odds Ratio
  intercept_b_odds <- exp(-0.6835)
  sl_1_odds <- exp(0.1399)
  
  print(intercept_b_odds)
  print(sl_1_odds)
}

# Sociability
{
  sociability_table <- coded_sifted %>%
    count(Sociability, `Sequel Purchased?`) %>%
    pivot_wider(names_from = `Sequel Purchased?`, values_from = n, values_fill = 0) %>%
    rename(Purchased = `1`, Churned = `0`) %>%
    mutate(
      Total = Churned + Purchased,
      Percentage = paste0(round(Total / 359 * 100, 2), "%"),
      Sociability = as.character(Sociability)
    ) %>%
    mutate(
      Sociability = case_when(  # Rename "0" and "1" 
        Sociability == 0 ~ "Non-Positive",
        Sociability == 1 ~ "Positive",
        TRUE ~ Sociability  # Deal with other possible values
      )
    )
  
  # Set summary_row to calculate only numeric variables
  summary_row3 <- sociability_table %>%
    summarise(across(where(is.numeric), sum)) %>%
    mutate(Sociability = "Total", Percentage = "100%")
  
  sociability_table <- bind_rows(sociability_table, summary_row3)
  sociability_table
  
  # chi-squared
  sociability_chisq <- chisq.test(matrix(c(194, 95, 43, 27), nrow = 2, byrow = TRUE))
  print(sociability_chisq)
  
  sc_long <- data.frame(
    Sociability = rep(c("Non-Positive", "Positive"), c(289, 70)),
    Purchased = c(rep(0, 194), rep(1, 95), rep(0, 43), rep(1, 27))
  )
  
  # Fits a logistic regression model
  model <- glm(Purchased ~ Sociability, data = sc_long, family = binomial)
  
  summary(model)
  
  confint(model)
  
  # Count Odds Ratio
  intercept_c_odds <- exp(-0.7140)
  sc_1_odds <- exp(0.2486)
  
  print(intercept_c_odds)
  print(sc_1_odds)
}

# Scariness
{
  scariness_table <- coded_sifted %>%
    count(Scariness, `Sequel Purchased?`) %>%
    pivot_wider(names_from = `Sequel Purchased?`, values_from = n, values_fill = 0) %>%
    rename(Purchased = `1`, Churned = `0`) %>%
    mutate(
      Total = Churned + Purchased,
      Percentage = paste0(round(Total / 359 * 100, 2), "%"),
      Scariness = as.character(Scariness)
    ) %>%
    mutate(
      Scariness = case_when(  # Rename "0" and "1" 
        Scariness == 0 ~ "Non-Positive",
        Scariness == 1 ~ "Positive",
        TRUE ~ Scariness  # Deal with other possible values
      )
    )
  
  # Set summary_row to calculate only numeric variables
  summary_row4 <- scariness_table %>%
    summarise(across(where(is.numeric), sum)) %>%
    mutate(Scariness = "Total", Percentage = "100%")
  
  scariness_table <- bind_rows(scariness_table, summary_row4)
  scariness_table
  
  # chi-squared
  scariness_chisq <- chisq.test(matrix(c(217, 102, 20, 20), nrow = 2, byrow = TRUE))
  print(scariness_chisq)
  
  scr_long <- data.frame(
    Scariness = rep(c("Non-Positive", "Positive"), c(319, 40)),
    Purchased = c(rep(0, 217), rep(1, 102), rep(0, 20), rep(1, 20))
  )
  
  # Fits a logistic regression model
  model <- glm(Purchased ~ Scariness, data = scr_long, family = binomial)
  
  summary(model)
  
  confint(model)
  
  # Count Odds Ratio
  intercept_d_odds <- exp(-0.7549)
  scr_1_odds <- exp(0.7549)
  
  print(intercept_d_odds)
  print(scr_1_odds)
}

# output tables
{
  # list the tables
  tables_list <- list(
    gameplay_table, storyline_table, sociability_table, scariness_table
  )
  
  # create an Excel file with each table as a sheet
  write_xlsx(tables_list, "Project_Tables.xlsx")
}

{
# Fitting a logistic regression model
model <- glm(`Sequel Purchased?` ~ Gameplay + Storyline + Sociability + Scariness, 
             data = coded_sifted, 
             family = binomial)
  
  new_data <- data.frame(
    Gameplay = c(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
    Storyline = c(0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1),
    Sociability = c(0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1),
    Scariness = c(0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0)
  )
  
  new_data$Purchased_Probability <- predict(model, newdata = new_data, type = "response")
  
  print(new_data)
  
  write_xlsx(new_data, "Purchase_Predict.xlsx")
  
# Calculate 95% CI and odds ratio
  exp(coef(model))
  exp(confint(model))
  
  model_summary <- summary(model)
  
  tidy_model <- broom::tidy(model, conf.int = TRUE, exponentiate = TRUE)
  
  # 绘制比值比图
  ggplot(tidy_model %>% filter(term != "(Intercept)"),
         aes(x = term, y = estimate, ymin = conf.low, ymax = conf.high)) +
    geom_pointrange() +  # 点表示比值比，线表示置信区间
    geom_hline(yintercept = 1, linetype = "dashed", color = "red") +  # 参考线
    coord_flip() +  # 翻转坐标轴for better readability
    labs(title = "Odds Ratios with 95% CI",
         y = "Odds Ratio", x = "") +
    theme_minimal()
  
  
# Extract model coefficients 
coefficients <- tidy_model
print(coefficients)
}
