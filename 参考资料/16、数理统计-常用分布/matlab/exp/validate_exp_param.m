function validate_exp_param(lambda)
%VALIDATE_EXP_PARAM 检查 λ 是否为正数

    if ~isscalar(lambda) || lambda <= 0
        error('λ (lambda) 必须为正数');
    end
end
