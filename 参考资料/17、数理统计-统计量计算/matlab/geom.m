function geom(p)
%GEOM 几何分布的常用统计量与图像展示
%
% 输入参数:
%   p - 成功概率 (0 < p <= 1)

    % 输入校验
    if ~isscalar(p) || p <= 0 || p > 1
        error('p 必须在 (0, 1] 区间内');
    end

    % k 的取值范围（显示前 maxK 项）
    maxK = 20;
    k = 1:maxK;

    % 概率质量函数 PMF
    pmf = (1 - p).^(k - 1) * p;

    % 累积分布函数 CDF
    cdf = 1 - (1 - p).^k;

    % 基本统计量
    EX = 1 / p;
    VarX = (1 - p) / p^2;
    StdX = sqrt(VarX);
    CoefVar = StdX / EX;
    Skew = (2 - p) / sqrt(1 - p);
    Kurt = 6 + p^2 / (1 - p);

    % 输出
    fprintf('几何分布 X ~ Geom(p = %.2f)\n', p);
    fprintf('期望 E[X] = %.2f\n', EX);
    fprintf('方差 Var[X] = %.2f\n', VarX);
    fprintf('标准差 Std[X] = %.2f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 图像展示
    figure;
    subplot(1, 2, 1);
    stem(k, pmf, 'filled');
    xlabel('k'); ylabel('P(X = k)');
    title('PMF of Geometric Distribution');

    subplot(1, 2, 2);
    stairs(k, cdf, 'LineWidth', 1.5);
    xlabel('k'); ylabel('P(X \leq k)');
    title('CDF of Geometric Distribution');
end
