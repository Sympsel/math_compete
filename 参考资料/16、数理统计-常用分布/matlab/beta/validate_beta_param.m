function validate_beta_param(alpha, beta)
%VALIDATE_BETA_PARAM 检查贝塔分布参数合法性

    if ~isscalar(alpha) || alpha <= 0 || ...
       ~isscalar(beta) || beta <= 0
        error('alpha 和 beta 必须为正标量');
    end
end
