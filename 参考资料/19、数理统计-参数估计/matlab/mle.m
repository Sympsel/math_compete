function [best_param, max_loglik] = mle(xs, param_grid, pmf_or_pdf)
    % mle_generic - 对任意分布进行参数的极大似然估计（MLE，网格搜索法）
    %
    % 输入参数：
    %   xs : vector
    %       观测样本
    %   param_grid : vector
    %       需要搜索的参数点（如[0.1, 0.2, ..., 0.9]），单参数为一维向量，多参数为元组向量
    %   pmf_or_pdf : function handle
    %       输入 x, theta，返回概率密度或概率质量（如 f(x, theta)）
    %
    % 输出：
    %   best_param : 最优参数 θ^
    %   max_loglik : 最大似然值 max_loglikelihood

    best_param = NaN; % 初始化最佳参数
    max_loglik = -Inf; % 初始化最大对数似然值

    % 遍历参数网格
    for i = 1:length(param_grid)
        theta = param_grid(i);
        loglik = 0.0;

        % 计算对数似然值
        for j = 1:length(xs)
            x = xs(j);
            p = pmf_or_pdf(x, theta);

            % 防止 log(0) 出错
            if p <= 0
                loglik = -Inf;
                break;
            end
            
            loglik = loglik + log(p);
        end

        % 更新最大对数似然值和最佳参数
        if loglik > max_loglik
            max_loglik = loglik;
            best_param = theta;
        end
    end
end
