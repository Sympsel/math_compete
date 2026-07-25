function p = t_cdf(t, df, steps)
    % 计算t分布的累积分布函数（CDF）
    if nargin < 3
        steps = 10000; % 默认步数
    end
    
    % t分布的概率密度函数
    function pdf = t_pdf(x, df)
        num = gamma((df + 1) / 2);
        den = sqrt(df * pi) * gamma(df / 2);
        pdf = num / den * (1 + x.^2 / df).^(-(df + 1) / 2);
    end

    a = -20; % 积分下限
    b = t;   % 积分上限
    h = (b - a) / steps;
    area = 0.5 * (t_pdf(a, df) + t_pdf(b, df));
    
    % 梯形法累加积分
    for i = 1:steps-1
        area = area + t_pdf(a + i * h, df);
    end
    p = area * h;
end

function [t_stat, df, p, reject] = t_test_1samp(xs, mu0, alpha, alternative)
    % 单样本t检验
    if nargin < 3
        alpha = 0.05; % 默认显著性水平
    end
    if nargin < 4
        alternative = 'two-sided'; % 默认双尾检验
    end
    
    n = length(xs);
    xbar = mean(xs); % 样本均值
    s = std(xs, 1); % 样本标准差（无偏估计）
    
    % 计算t统计量
    t_stat = (xbar - mu0) / (s / sqrt(n));
    df = n - 1; % 自由度
    cdf_val = t_cdf(t_stat, df); % 累积概率
    
    % 计算p值
    if strcmp(alternative, 'two-sided')
        p = 2 * min(cdf_val, 1 - cdf_val);
    elseif strcmp(alternative, 'less')
        p = cdf_val;
    elseif strcmp(alternative, 'greater')
        p = 1 - cdf_val;
    else
        error("alternative 仅能取 'two-sided', 'less', 'greater'");
    end
    
    reject = p < alpha; % 是否拒绝原假设
end

function [t_stat, df, p, reject] = t_test_ind(xs1, xs2, alpha, alternative, equal_var)
    % 独立样本t检验
    if nargin < 3
        alpha = 0.05; % 默认显著性水平
    end
    if nargin < 4
        alternative = 'two-sided'; % 默认双尾检验
    end
    if nargin < 5
        equal_var = true; % 默认假定方差相等
    end
    
    n1 = length(xs1);
    n2 = length(xs2);
    mean1 = mean(xs1);
    mean2 = mean(xs2);
    
    % 计算方差
    s2_1 = var(xs1, 1); % 样本方差
    s2_2 = var(xs2, 1);
    
    if equal_var
        % 方差相等
        sp2 = ((n1 - 1) * s2_1 + (n2 - 1) * s2_2) / (n1 + n2 - 2);
        se = sqrt(sp2 * (1/n1 + 1/n2));
        t_stat = (mean1 - mean2) / se;
        df = n1 + n2 - 2;
    else
        % 方差不等
        se = sqrt(s2_1 / n1 + s2_2 / n2);
        t_stat = (mean1 - mean2) / se;
        
        % Welch–Satterthwaite公式
        numerator = (s2_1 / n1 + s2_2 / n2)^2;
        denominator = (s2_1 / n1)^2 / (n1 - 1) + (s2_2 / n2)^2 / (n2 - 1);
        df = numerator / denominator;
    end
    
    % 计算累积概率
    cdf_val = t_cdf(t_stat, df);
    if strcmp(alternative, 'two-sided')
        p = 2 * min(cdf_val, 1 - cdf_val);
    elseif strcmp(alternative, 'less')
        p = cdf_val;
    elseif strcmp(alternative, 'greater')
        p = 1 - cdf_val;
    else
        error("alternative 仅能取 'two-sided', 'less', 'greater'");
    end
    
    reject = p < alpha; % 是否拒绝原假设
end

function [t_stat, df, p, reject] = t_test_paired(xs1, xs2, alpha, alternative)
    % 配对样本t检验
    if length(xs1) ~= length(xs2)
        error("两组样本数量必须一致（配对样本）");
    end
    
    n = length(xs1);
    ds = xs1 - xs2; % 差值
    d_bar = mean(ds);
    s_d = std(ds, 1); % 差值的标准差
    
    % 计算t统计量
    t_stat = d_bar / (s_d / sqrt(n));
    df = n - 1;
    cdf_val = t_cdf(t_stat, df);
    
    if strcmp(alternative, 'two-sided')
        p = 2 * min(cdf_val, 1 - cdf_val);
    elseif strcmp(alternative, 'less')
        p = cdf_val;
    elseif strcmp(alternative, 'greater')
        p = 1 - cdf_val;
    else
        error("alternative 仅能取 'two-sided', 'less', 'greater'");
    end
    
    reject = p < alpha; % 是否拒绝原假设
end

% ==========================
% 示例
% ==========================
xs = [55, 52, 48, 50, 53, 56, 49, 51, 58, 54];
mu0 = 50.0;
[t_stat, df, p, reject] = t_test_1samp(xs, mu0, 0.05, 'greater');
fprintf('单样本t检验：\nt统计量 = %.4f\n自由度 = %d\np值 = %.4f\n结论：%s\n\n', ...
        t_stat, df, p, ifelse(reject, '拒绝H0', '不拒绝H0'));

xs1 = [65, 68, 70, 63, 72, 67, 69, 71, 64, 66];
xs2 = [82, 78, 85, 80, 83, 77, 86, 79, 84, 81];
[t_stat, df, p, reject] = t_test_ind(xs1, xs2, 0.05, 'less', true);
fprintf('独立样本t检验：\nt统计量 = %.4f\n自由度 = %.2f\np值 = %.4f\n结论：%s\n\n', ...
        t_stat, df, p, ifelse(reject, '拒绝H0', '不拒绝H0'));

xs1 = [45, 60, 50, 55, 40, 65, 48, 70, 52, 58];
xs2 = [20, 25, 18, 28, 22, 30, 26, 15, 23, 19];
[t_stat, df, p, reject] = t_test_paired(xs1, xs2, 0.05, 'greater');
fprintf('配对样本t检验：\nt统计量 = %.4f\n自由度 = %d\np值 = %.4f\n结论：%s\n', ...
        t_stat, df, p, ifelse(reject, '拒绝H0', '不拒绝H0'));

function result = ifelse(condition, trueValue, falseValue)
    % 自定义的ifelse函数
    if condition
        result = trueValue;
    else
        result = falseValue;
    end
end
