function hypergeom(N, M, n)
%HYPERGEOM_DIST 计算并展示超几何分布的常用统计量与图像
%
% 输入参数：
%   N - 总体总数（正整数）
%   M - 成功元素个数（0 <= M <= N）
%   n - 抽样数量（0 <= n <= N）

    % 输入参数校验
    if ~isscalar(N) || N <= 0 || mod(N, 1) ~= 0
        error('N 必须为正整数');
    end
    if ~isscalar(M) || M < 0 || M > N || mod(M, 1) ~= 0
        error('M 必须为 0 到 N 之间的整数');
    end
    if ~isscalar(n) || n < 0 || n > N || mod(n, 1) ~= 0
        error('n 必须为 0 到 N 之间的整数');
    end

    % 有效的 k 范围：max(0, n+M-N) 到 min(n, M)
    k_low = max(0, n + M - N);
    k_high = min(n, M);
    k = k_low:k_high;

    % PMF & CDF
    pmf = hygepdf(k, N, M, n);
    cdf = hygecdf(k, N, M, n);

    % 统计量计算
    EX = n * (M / N);
    VarX = n * (M / N) * (1 - M / N) * (N - n) / (N - 1);
    StdX = sqrt(VarX);
    CoefVar = StdX / EX;
    
    % 使用原点矩和中心矩估算偏度与峰度
    raw3 = sum((k .^ 3) .* pmf);
    central3 = sum(((k - EX) .^ 3) .* pmf);
    central4 = sum(((k - EX) .^ 4) .* pmf);
    
    Skew = central3 / StdX^3;
    Kurt = central4 / StdX^4;

    % 控制台输出
    fprintf('超几何分布 X ~ HG(N=%d, M=%d, n=%d)\n', N, M, n);
    fprintf('期望 E[X] = %.4f\n', EX);
    fprintf('方差 Var[X] = %.4f\n', VarX);
    fprintf('标准差 Std[X] = %.4f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 图像展示
    figure;
    subplot(1, 2, 1);
    stem(k, pmf, 'filled');
    xlabel('k'); ylabel('P(X = k)');
    title('PMF of Hypergeometric Distribution');

    subplot(1, 2, 2);
    stairs(k, cdf, 'LineWidth', 1.5);
    xlabel('k'); ylabel('P(X ≤ k)');
    title('CDF of Hypergeometric Distribution');
end
