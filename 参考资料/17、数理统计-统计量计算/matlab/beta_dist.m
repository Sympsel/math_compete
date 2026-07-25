function beta_dist(alpha, beta)
%BETA_DIST 计算并展示贝塔分布的常用统计量与图像
%
% 输入参数:
%   alpha - 形状参数 α > 0
%   beta  - 形状参数 β > 0

    % 参数校验
    if ~isscalar(alpha) || alpha <= 0
        error('alpha 必须是正数');
    end
    if ~isscalar(beta) || beta <= 0
        error('beta 必须是正数');
    end

    % 自变量范围
    x = linspace(0, 1, 1000);

    % 概率密度函数
    pdf = betapdf(x, alpha, beta);

    % 累积分布函数
    cdf = betacdf(x, alpha, beta);

    % 期望与方差
    EX = alpha / (alpha + beta);
    VarX = (alpha * beta) / ((alpha + beta)^2 * (alpha + beta + 1));
    StdX = sqrt(VarX);
    CoefVar = StdX / EX;

    % 偏度
    Skew = 2 * (beta - alpha) * sqrt(alpha + beta + 1) ...
           / ((alpha + beta + 2) * sqrt(alpha * beta));

    % 峰度
    excess_kurt = 6 * ((alpha - beta)^2 * (alpha + beta + 1) - alpha * beta * (alpha + beta + 2)) ...
                  / (alpha * beta * (alpha + beta + 2) * (alpha + beta + 3));
    Kurt = excess_kurt + 3;

    % 输出统计量
    fprintf('贝塔分布 X ~ Beta(α = %.2f, β = %.2f)\n', alpha, beta);
    fprintf('期望 E[X] = %.4f\n', EX);
    fprintf('方差 Var[X] = %.4f\n', VarX);
    fprintf('标准差 Std[X] = %.4f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 绘图
    figure;

    subplot(1, 2, 1);
    plot(x, pdf, 'LineWidth', 2);
    xlabel('x'); ylabel('f(x)');
    title('PDF of Beta Distribution');
    xlim([0 1]); ylim([0 max(pdf) * 1.1]);

    subplot(1, 2, 2);
    plot(x, cdf, 'LineWidth', 2);
    xlabel('x'); ylabel('P(X \leq x)');
    title('CDF of Beta Distribution');
    xlim([0 1]); ylim([0 1.05]);
end
