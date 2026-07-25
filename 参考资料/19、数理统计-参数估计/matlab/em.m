% 生成数据
rng(0); % 为了可重复性
n = 300; % 数据点数量
mu1 = 2; % 第一个高斯分布的均值
sigma1 = 0.5; % 第一个高斯分布的标准差
mu2 = 5; % 第二个高斯分布的均值
sigma2 = 1; % 第二个高斯分布的标准差

% 生成混合高斯数据
data = [normrnd(mu1, sigma1, n/2, 1); normrnd(mu2, sigma2, n/2, 1)];

% 初始化参数
mu = [1; 4]; % 初始均值
sigma = [1; 1]; % 初始标准差
pi = [0.5; 0.5]; % 初始混合权重

% EM 算法
max_iter = 100; % 最大迭代次数
tol = 1e-6; % 收敛阈值

for iter = 1:max_iter
    % E 步骤：计算责任度
    resp = zeros(n, 2);
    for j = 1:2
        resp(:, j) = pi(j) * normpdf(data, mu(j), sigma(j));
    end
    resp = resp ./ sum(resp, 2); % 归一化

    % M 步骤：更新参数
    Nk = sum(resp, 1); % 每个分布的责任
    mu_new = (resp' * data) ./ Nk'; % 更新均值
    sigma_new = sqrt((resp' * (data.^2)) ./ Nk' - mu_new.^2); % 更新标准差
    pi_new = Nk / n; % 更新混合权重

    % 检查收敛
    if max(abs(mu_new - mu)) < tol && max(abs(sigma_new - sigma)) < tol && max(abs(pi_new - pi)) < tol
        break;
    end

    % 更新参数
    mu = mu_new;
    sigma = sigma_new;
    pi = pi_new;
end

% 输出结果
fprintf('估计的均值：\n');
disp(mu);
fprintf('估计的标准差：\n');
disp(sigma);
fprintf('估计的混合权重：\n');
disp(pi);
