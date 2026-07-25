function norm_dist(mu, sigma)
%NORM_DIST 计算并绘制正态分布的主要性质
%
% 输入参数:
%   mu    - 均值 (任意实数)
%   sigma - 标准差 (正数)

    % 参数校验
    if ~isscalar(mu)
        error('mu 必须是标量');
    end
    if ~isscalar(sigma) || sigma <= 0
        error('sigma 必须为正数');
    end

    % 定义绘图区间
    x = linspace(mu - 5 * sigma, mu + 5 * sigma, 1000);

    % 概率密度函数
    pdf = (1 / (sigma * sqrt(2 * pi))) * exp(-((x - mu).^2) / (2 * sigma^2));

    % 累积分布函数
    cdf = 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))));

    % 基本统计量
    EX = mu;
    VarX = sigma^2;
    StdX = sigma;
    CoefVar = StdX / EX;
    Skew = 0;        % 正态分布偏度为 0
    Kurt = 3;        % 正态分布峰度为 3

    % 输出统计量
    fprintf('正态分布 X ~ N(%.2f, %.2f^2)\n', mu, sigma);
    fprintf('期望 E[X] = %.4f\n', EX);
    fprintf('方差 Var[X] = %.4f\n', VarX);
    fprintf('标准差 Std[X] = %.4f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 绘图展示
    figure;

    subplot(1, 2, 1);
    plot(x, pdf, 'LineWidth', 2);
    xlabel('x'); ylabel('f(x)');
    title('PDF of Normal Distribution');

    subplot(1, 2, 2);
    plot(x, cdf, 'LineWidth', 2);
    xlabel('x'); ylabel('P(X \leq x)');
    title('CDF of Normal Distribution');
end
