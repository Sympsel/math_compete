function expon(lambda)
%EXPONENTIAL_DIST 计算并展示指数分布的主要性质与图像
%
% 输入参数:
%   lambda - 指数分布的速率参数 λ，必须大于 0

    % 参数校验
    if ~isscalar(lambda) || lambda <= 0
        error('lambda 必须为正数');
    end

    % 定义绘图范围
    x = linspace(0, 8 / lambda, 1000);  % 以均值的8倍为上限

    % 概率密度函数 PDF
    pdf = lambda * exp(-lambda * x);

    % 累积分布函数 CDF
    cdf = 1 - exp(-lambda * x);

    % 统计量计算
    EX = 1 / lambda;                  % 期望
    VarX = 1 / lambda^2;              % 方差
    StdX = sqrt(VarX);                % 标准差
    CoefVar = StdX / EX;              % 变异系数
    Skew = 2;                         % 偏度
    Kurt = 9;                         % 峰度（含3）

    % 显示统计量
    fprintf('指数分布 X ~ Exp(lambda = %.2f)\n', lambda);
    fprintf('期望 E[X] = %.4f\n', EX);
    fprintf('方差 Var[X] = %.4f\n', VarX);
    fprintf('标准差 Std[X] = %.4f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 绘图展示
    figure;

    % PDF 图像
    subplot(1, 2, 1);
    plot(x, pdf, 'LineWidth', 2);
    xlabel('x'); ylabel('f(x)');
    title('PDF of Exponential Distribution');
    xlim([0, max(x)]); ylim([0, max(pdf) * 1.1]);

    % CDF 图像
    subplot(1, 2, 2);
    plot(x, cdf, 'LineWidth', 2);
    xlabel('x'); ylabel('P(X \leq x)');
    title('CDF of Exponential Distribution');
    xlim([0, max(x)]); ylim([0, 1.05]);
end
