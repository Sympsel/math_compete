function [p, reject] = basic_hypothesis_test(T_obs, T_null_dist, alpha, alternative)
    % 基础假设检验（右尾、左尾、双尾）
    % 参数
    % T_obs : 实际观测到的检验统计量
    % T_null_dist : H0（原假设）下，统计量T的模拟分布
    % alpha : 显著性水平（默认0.05）
    % alternative : 'greater'，'less'，'two-sided'
    
    if nargin < 3
        alpha = 0.05; % 默认显著性水平
    end
    if nargin < 4
        alternative = 'two-sided'; % 默认双侧检验
    end
    
    n = length(T_null_dist);
    
    if strcmp(alternative, 'greater')
        % 右尾检验
        p = sum(T_null_dist >= T_obs) / n;
    elseif strcmp(alternative, 'less')
        % 左尾检验
        p = sum(T_null_dist <= T_obs) / n;
    elseif strcmp(alternative, 'two-sided')
        % 双尾检验
        T_mean = mean(T_null_dist);
        diff = abs(T_obs - T_mean);
        p = sum(abs(T_null_dist - T_mean) >= diff) / n;
    else
        error("alternative 只能取 'greater', 'less', 'two-sided'");
    end
    
    reject = p < alpha; % 是否拒绝原假设
end

% ==========================
% 示例：检验一组样本的均值是否大于/小于、等于72
% ==========================
rng(0); % 设置随机种子
% 原假设：均值为72，检验统计量T为均值
T_obs = 75;
% H0下分布：生成10000组N(72,10)样本（理论均值为72）
T_null_dist = arrayfun(@(x) mean(normrnd(72, 10, [100, 1])), 1:10000);
% 单尾左侧检验
[p, reject] = basic_hypothesis_test(T_obs, T_null_dist, 0.05, 'two-sided');

% 输出结果
fprintf('观测统计量 T_obs = %.3f\n', T_obs);
fprintf('p值 = %.4f\n', p);
if reject
    fprintf('结论：拒绝H0\n');
else
    fprintf('结论：不拒绝H0\n');
end