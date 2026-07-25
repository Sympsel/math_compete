function binom(n, p)
%BINOMIAL_DIST 计算并展示二项分布的常用统计量与图像
%
% 输入参数:
%   n - 重复试验次数 (正整数)
%   p - 单次试验成功概率 (0 <= p <= 1)

    % 输入校验
    if ~isscalar(n) || n <= 0 || mod(n,1) ~= 0
        error('n 必须是正整数');
    end
    if ~isscalar(p) || p < 0 || p > 1
        error('p 必须在 [0, 1] 区间内');
    end

    % k 的取值范围
    k = 0:n;

    % 概率质量函数 PMF
    pmf = binopdf(k, n, p);

    % 累积分布函数 CDF
    cdf = binocdf(k, n, p);

    % 基本统计量
    EX = n * p;
    VarX = n * p * (1 - p);
    StdX = sqrt(VarX);
    CoefVar = StdX / EX;
    Skew = (1 - 2 * p) / StdX;
    Kurt = (1 - 6 * p * (1 - p)) / VarX + 3;

    % 输出
    fprintf('二项分布 X ~ Bin(n = %d, p = %.2f)\n', n, p);
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
    title('PMF of Binomial Distribution');

    subplot(1, 2, 2);
    stairs(k, cdf, 'LineWidth', 1.5);
    xlabel('k'); ylabel('P(X ≤ k)');
    title('CDF of Binomial Distribution');
end
