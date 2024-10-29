import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

def perform_anova(df):
    model = ols('value ~ C(variable)', data=df.melt(var_name='variable', value_name='value')).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table