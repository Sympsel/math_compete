function poisson(lambda)
%POISSON_DIST 用于计算泊松分布的统计量与图像
%
% 输入:
%   lambda - 泊松分布的 λ 参数 (λ > 0)

    % 参数校验
    if lambda <= 0
        error('参数 lambda 必须大于 0');
    end

    % 取值范围根据 λ 自动扩展
    k_max = ceil(lambda + 5 * sqrt(lambda));
    k = 0:k_max;

    % 概率质量函数 (PMF)
    pmf = poisspdf(k, lambda);

    % 累积分布函数 (CDF)
    cdf = poisscdf(k, lambda);

    % 基本统计量
    EX = lambda;
    VarX = lambda;
    StdX = sqrt(lambda);
    CoefVar = StdX / EX;
    Skew = 1 / StdX;
    Kurt = 1 / lambda + 3;

    % 输出结果
    fprintf('泊松分布 X ~ Poisson(%.2f)\n', lambda);
    fprintf('期望 E[X] = %.2f\n', EX);
    fprintf('方差 Var[X] = %.2f\n', VarX);
    fprintf('标准差 Std[X] = %.2f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 可视化
    figure;
    subplot(1, 2, 1);
    stem(k, pmf, 'filled');
    xlabel('k'); ylabel('P(X = k)');
    title('PMF of Poisson Distribution');

    subplot(1, 2, 2);
    stairs(k, cdf, 'LineWidth', 1.5);
    xlabel('k'); ylabel('P(X ≤ k)');
    title('CDF of Poisson Distribution');

end
