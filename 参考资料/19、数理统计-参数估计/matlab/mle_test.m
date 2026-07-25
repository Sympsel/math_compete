% 已知的参数
n = 10; % 试验次数
k = 7;  % 成功次数

% 设置 p 的搜索范围
p_grid = linspace(0, 1, 100); % 在 0 到 1 之间取 100 个点

% 初始化概率数组
probabilities = zeros(size(p_grid));

% 计算每个 p 值对应的概率
for i = 1:length(p_grid)
    p = p_grid(i);
    probabilities(i) = nchoosek(n, k) * (p^k) * ((1 - p)^(n - k));
end

% 找到最大概率值和对应的 p
[max_probability, max_index] = max(probabilities);
estimated_p = p_grid(max_index);

% 输出结果
fprintf('对于 n = %d，成功次数 k = %d，估计的成功概率 p = %.4f，最大概率 P(X = %d) = %.4f\n', ...
        n, k, estimated_p, k, max_probability);
