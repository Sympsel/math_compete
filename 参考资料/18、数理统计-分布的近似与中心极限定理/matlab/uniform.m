function uniform(a, b)
%UNIFORM_DIST 计算并展示连续型均匀分布的主要性质
%
% 输入参数:
%   a - 分布区间下界 (实数)
%   b - 分布区间上界 (实数，需满足 b > a)

    % 参数校验
    if ~isscalar(a) || ~isscalar(b) || b <= a
        error('参数错误：要求 b > a，且 a、b 为标量');
    end

    % 定义绘图范围
    x = linspace(a - (b - a) * 0.2, b + (b - a) * 0.2, 1000);

    % 概率密度函数 PDF
    pdf = zeros(size(x));
    pdf(x >= a & x <= b) = 1 / (b - a);

    % 累积分布函数 CDF
    cdf = zeros(size(x));
    cdf(x < a) = 0;
    cdf(x > b) = 1;
    mask = (x >= a) & (x <= b);
    cdf(mask) = (x(mask) - a) / (b - a);

    % 基本统计量计算
    EX = (a + b) / 2;                      % 期望
    VarX = (b - a)^2 / 12;                 % 方差
    StdX = sqrt(VarX);                    % 标准差
    CoefVar = StdX / EX;                  % 变异系数
    Skew = 0;                             % 偏度
    Kurt = 1.8;                           % 峰度 = -6/5 + 3

    % 显示输出
    fprintf('均匀分布 X ~ U(%.2f, %.2f)\n', a, b);
    fprintf('期望 E[X] = %.4f\n', EX);
    fprintf('方差 Var[X] = %.4f\n', VarX);
    fprintf('标准差 Std[X] = %.4f\n', StdX);
    fprintf('变异系数 CV = %.4f\n', CoefVar);
    fprintf('偏度 Skew[X] = %.4f\n', Skew);
    fprintf('峰度 Kurt[X] = %.4f\n', Kurt);

    % 绘图展示
    figure;

    % 概率密度函数图
    subplot(1, 2, 1);
    plot(x, pdf, 'LineWidth', 2);
    xlabel('x'); ylabel('f(x)');
    title('PDF of Uniform Distribution');
    xlim([min(x), max(x)]); ylim([0, max(pdf) * 1.2]);

    % 累积分布函数图
    subplot(1, 2, 2);
    plot(x, cdf, 'LineWidth', 2);
    xlabel('x'); ylabel('P(X \leq x)');
    title('CDF of Uniform Distribution');
    xlim([min(x), max(x)]); ylim([0, 1.05]);
end
