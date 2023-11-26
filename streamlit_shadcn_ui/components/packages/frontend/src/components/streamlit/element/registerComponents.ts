
import { StButton } from "../button";
import { StCard } from "../card"
import { StInput } from "../input";

const ComponentCollection = {
    card: StCard,
    button: StButton,
    input: StInput,
} as const;

export function getComponent (componentName: string) {
    if (componentName in ComponentCollection) {
        return ComponentCollection[componentName]
    }
    return false
}