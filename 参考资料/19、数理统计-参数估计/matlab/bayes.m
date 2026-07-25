% 观测数据
xs = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

% 均匀分布先验（Uniform(0,1)）
prior = @(p) (0 <= p && p <= 1);

% 伯努利似然
likelihood = @(xs, p) (prod(p.^xs) * prod((1 - p).^(1 - xs)));

% 参数网格
theta_grid = (1:99) / 100; % [0.01, 0.02, ..., 0.99]
posterior = zeros(size(theta_grid)); % 初始化后验分布
total = 0; % 总概率

% 计算后验分布
for i = 1:length(theta_grid)
    theta = theta_grid(i);
    if prior(theta)
        prob = prior(theta) * likelihood(xs, theta);
        posterior(i) = prob;
        total = total + prob;
    end
end

% 归一化
posterior = posterior / total;

% 后验均值
post_mean = sum(theta_grid .* posterior);

% 输出结果
fprintf('均匀先验下后验均值估计 = %.4f\n', post_mean);
