function gamma_dist(k, lambda)
%GAMMA_DIST 计算并展示伽马分布的常用统计量与图像
%
% 输入参数:
%   k      - 形状参数 (k > 0)
%   lambda - 速率参数 λ (lambda > 0)

    % 参数校验
    if ~isscalar(k) || k <= 0
        error('形状参数 k 必须为正数');
    end
    if ~isscalar(lambda) || lambda <= 0
        error('速率参数 lambda 必须为正数');
    end

    % 定义绘图范围
    x = linspace(0, gaminv(0.999, k, 1/lambda), 1000);  % 最大值为99.9%分位点

    % 概率密度函数 PDF
    pdf = gampdf(x, k, 1/lambda);

    % 累积分布函数 CDF
    cdf = gamcdf(x, k, 1/lambda);

    % 统计量
    EX = k / lambda;
    VarX = k / lambda^2;
    StdX = sqrt(VarX);
    CoefVar = StdX / EX;
    Skew = 2 / sqrt(k);
    Kurt = 6 / k + 3;

    % 输出统计量
    fprintf('伽马分布 X ~ Gamma(k = %.2f, lambda = %.2f)\n', k, lambda);
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
    title('PDF of Gamma Distribution');
    xlim([0, max(x)]); ylim([0, max(pdf)*1.1]);

    subplot(1, 2, 2);
    plot(x, cdf, 'LineWidth', 2);
    xlabel('x'); ylabel('P(X \leq x)');
    title('CDF of Gamma Distribution');
    xlim([0, max(x)]); ylim([0, 1.05]);
end
