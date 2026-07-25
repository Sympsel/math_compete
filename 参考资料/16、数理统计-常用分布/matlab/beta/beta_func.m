function B = beta_func(alpha, beta)
%BETA_FUNC 计算贝塔函数 B(α, β) = Γ(α) * Γ(β) / Γ(α + β)

    B = gamma(alpha) * gamma(beta) / gamma(alpha + beta);
end
